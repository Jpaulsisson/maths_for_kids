import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({
  weight: ['100', '400', '700', '900'],
  subsets: ['latin']
})

export const metadata: Metadata = {
  title: 'Maths for Kids',
  description: 'Unlimited Math Problems for Practicing',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
