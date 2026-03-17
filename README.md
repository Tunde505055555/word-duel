# Word Duel — GenLayer AI Mini Game

An on-chain word category game powered by a GenLayer Intelligent Contract.
Submit words, the AI judges if they fit the category, 5 validators reach consensus.

## Project Structure
```
vigil-game/
├── contracts/
│   └── word_duel.py
├── deploy/
│   └── deployScript.ts
├── frontend/
│   ├── src/app/
│   │   ├── page.tsx
│   │   └── layout.tsx
│   ├── package.json
│   ├── next.config.js
│   └── .env.example
└── README.md
```

## Requirements

- Node.js 18+
- GenLayer CLI: `npm install -g genlayer`
- A GenLayer testnet account (get one at studio.genlayer.com)

## Step 1 — Deploy the Contract
```bash
genlayer network
genlayer deploy
```

Copy the deployed contract address from the output.

## Step 2 — Setup Frontend
```bash
cd frontend
cp .env.example .env
```

Edit `.env`:
```
NEXT_PUBLIC_GENLAYER_RPC_URL=https://studio.genlayer.com:8443/api
NEXT_PUBLIC_CONTRACT_ADDRESS=0x_your_deployed_address_here
```

## Step 3 — Run
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000

## Step 4 — Deploy to Vercel
```bash
cd frontend
npx vercel --prod
```

## How to Play

1. The game shows the current category
2. Type any word and click Submit
3. 5 GenLayer validators run an LLM to judge your word
4. Consensus is reached — PASS or FAIL recorded on-chain

## GenLayer Tech Used

- gl.exec_prompt() — on-chain LLM reasoning
- gl.eq_principle_strict_eq — strict validator consensus
- GenLayer JSON-RPC — gen_call for reads, gen_sendTransaction for writes
