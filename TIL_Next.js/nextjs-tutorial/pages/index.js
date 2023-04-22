import Axios from "axios";
import Head from 'next/head';
import ItemList from "../src/component/ItemList";
import styles from '../styles/Home.module.css';
import { useEffect, useState } from 'react';

export default function Home() {
  const [list, setList] = useState([])
  const API_URL = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline";

  function getData() {
    Axios.get(API_URL).then((res) => {
      console.log(res.data)
      setList(res.data)
    })
  }

  useEffect(() => {
    getData()
  }, [])
  

  return (
    <div>
      <Head>
        <title>HOME | 코딩앙마</title>
      </Head>
      <Header as="h3" style={{ paddingTop: 40 }}>
        베스트 상품
      </Header>
      <Divider />
      <ItemList list={list} />
    </div>
  )
}
