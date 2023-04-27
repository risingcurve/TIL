import Axios from "axios";
import Head from 'next/head';
import ItemList from "../src/component/ItemList";
import { Header, Divider, Loader } from 'semantic-ui-react';
import styles from '../styles/Home.module.css';
import { useEffect, useState } from 'react';

// export default function Home() {
//   const [list, setList] = useState([])
//   const [isLoading, setIsLoading] = useState(true)

//   const API_URL = process.env.NEXT_PUBLIC_API_URL

//   // const API_URL = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline";

//   function getData() {
//     Axios.get(API_URL).then((res) => {
//       console.log(res.data)
//       setList(res.data)
//       setIsLoading(false)
//     })
//   }

//   useEffect(() => {
//     getData()
//   }, [])
  

//   return (
//     <div>
//       <Head>
//         <title>HOME | 코딩앙마</title>
//         <meta name="description" content="코딩 앙마 홈입니다."></meta>
//       </Head>
//       {isLoading && (
//         <div style={{ padding: "300px 0" }}>
//           <Loader inline="centered" active>
//             Loading
//           </Loader>
//         </div>
//       )}
//       {!isLoading && (
//         <div>
//           <Header as="h3" style={{ paddingTop: 40 }}>
//             베스트 상품
//           </Header>
//           <Divider />
//           <ItemList list={list.slice(0, 9)} />
//           <Header as="h3" style={{ paddingTop: 40 }}>
//             신상품
//           </Header>
//           <Divider />
//           <ItemList list={list.slice(9)} />
//         </div>
//       )}
//     </div>
//   )
// }

export default function Home({ list }) {
  return (
    <div>
      <Head>
        <title>HOME | 코딩앙마</title>
        <meta name="description" content="코딩 앙마 홈입니다."></meta>
      </Head>
      <div>
        <Header as="h3" style={{ paddingTop: 40 }}>
          베스트 상품
        </Header>
        <Divider />
        <ItemList list={list.slice(0, 9)} />
        <Header as="h3" style={{ paddingTop: 40 }}>
          신상품
        </Header>
        <Divider />
        <ItemList list={list.slice(9)} />
      </div>
    </div>
  )
}

export async function getStaticProps() {
  // const apiUrl = process.env.NEXT_PUBLIC_API_URL
  const apiUrl = process.env.apiUrl
  const res = await Axios.get(apiUrl)
  const data = res.data

  return {
    props: {
      list: data,
      name: process.env.name,
    },
  }
}