import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <meta charSet="utf-8" />
        <meta name="description" content="Emotional Support Website - AI-powered emotional support assistant" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <body className="w-full overflow-x-hidden">
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
