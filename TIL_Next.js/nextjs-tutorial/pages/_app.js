import "../styles/globals.css"
import "semantic-ui-css/semantic.min.css"
import Footer from "../src/component/Footer"
import Top from "../src/component/Top"

import '@/styles/globals.css'

export default function App({ Component, pageProps }) {
  return (
    <div style={{ width: 1000, margin: "0 auto" }}>
      <Top />
      <Component {...pageProps} />
      <Footer />
    </div>
  )
}
