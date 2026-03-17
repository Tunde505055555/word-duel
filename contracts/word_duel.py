# { "Depends": "py-genlayer:test" }

from genlayer import *
import json


class WordDuel(gl.Contract):
    round_number: int
    total_correct: int
    last_word: str
    last_result: bool
    last_feedback: str
    current_category: str

    def __init__(self):
        self.round_number = 0
        self.total_correct = 0
        self.last_word = ""
        self.last_result = False
        self.last_feedback = ""
        self.current_category = "things you find in a kitchen"

    @gl.public.view
    def get_category(self) -> str:
        return self.current_category

    @gl.public.view
    def get_round(self) -> int:
        return self.round_number

    @gl.public.view
    def get_score(self) -> int:
        return self.total_correct

    @gl.public.view
    def get_last_word(self) -> str:
        return self.last_word

    @gl.public.view
    def get_last_result(self) -> bool:
        return self.last_result

    @gl.public.view
    def get_last_feedback(self) -> str:
        return self.last_feedback

    @gl.public.write
    def submit_word(self, word: str) -> None:
        self.round_number += 1
        self.last_word = word

        prompt = (
            "You are a judge in a word category game.\n\n"
            "Category: " + self.current_category + "\n"
            "Player's word: " + word + "\n\n"
            "Decide if the word clearly fits the category.\n"
            "Be reasonable — common sense answers should pass.\n"
            "Be strict about obvious wrong answers.\n\n"
            "Respond ONLY with this exact JSON, nothing else:\n"
            '{"correct": true/false, "feedback": "one sentence explanation"}\n\n'
            "It is mandatory that you respond only using the JSON format above, nothing else.\n"
            "Don't include any other words or characters, your output must be only JSON without any formatting prefix or suffix.\n"
            "This result should be perfectly parseable by a JSON parser without errors."
        )

        def nondet():
            res = gl.exec_prompt(prompt)
            res = res.replace("```json", "").replace("```", "").strip()
            dat = json.loads(res)
            return dat["correct"]

        correct = gl.eq_principle_strict_eq(nondet)
        assert isinstance(correct, bool)

        self.last_result = correct
        if correct:
            self.total_correct += 1
            self.last_feedback = "Correct! " + word + " fits the category."
        else:
            self.last_feedback = "Wrong! " + word + " does not fit: " + self.current_category

    @gl.public.write
    def change_category(self, new_category: str) -> None:
        self.current_category = new_category
        self.round_number = 0
        self.total_correct = 0
        self.last_word = ""
        self.last_result = False
        self.last_feedback = "New category set! Good luck."
