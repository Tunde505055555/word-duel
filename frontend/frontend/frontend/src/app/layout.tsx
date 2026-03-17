import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Word Duel — GenLayer AI Game',
  description: 'An on-chain AI word game powered by GenLayer Intelligent Contracts',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0 }}>{children}</body>
    </html>
  );
}
