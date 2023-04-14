// import "../styles/globals.css"
import '@/styles/globals.css'

export default function App({ Component, pageProps }) {
  return (
    <div>
      <Component {...pageProps} />
      <Footer />
    </div>

  )
}
