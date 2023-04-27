import Axios from "axios";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { Loader } from 'semantic-ui-react';
import Item from "../../src/component/Item"

const Post = ({ item, name }) => {
  const router = useRouter()

  if (router.isFallback) {
    return (
      <div style={{ padding: "100px 0"}}>
        <Loader active inline="centered">
          Loading
        </Loader>
      </div>
    )
  }

  return (
    <div>
      {item && (
      <div>
        <Head>
          <title>{item.name}</title>
          <meta name="description" content={item.description}></meta>
        </Head>
        {name} 환경입니다.
        <Item item={item} />
      </div>
      )}
    </div>
  )
}

export default Post

export async function getStaticPaths() {
  const apiUrl = process.env.apiUrl
  const res = await Axios.get(apiUrl)
  const data = res.data
  return {
    // paths: [
    //   { params: { id: '740'} },
    //   { params: { id: '730'} },
    //   { params: { id: '729'} },
    // ],
    paths : data.slice(0, 9).map(item => ({
      params : {
        id : item.id.toString(),
      }
    })),
    fallback: true,
  }
}

export async function getStaticProps(context) {
  const id = context.params.id
  const apiUrl = `http://makeup-api.herokuapp.com/api/v1/products/${id}.json`;
  const res = await Axios.get(apiUrl)
  const data = res.data

  return {
    props: {
      item: data,
      name: process.env.name
    },
  }
}





/* 
Next.js 모든 페이지 사전 렌더링
더 좋은 퍼포먼스
SEO

1. 정적 생성
2. SSR

차이점은 언제 html 파일을 생성하는가

[정적 생성]
- 프로젝트가 빌드하는 시점에 html 파일들이 생성
- 모든 요청에 재사용
- 퍼포먼스 이유로, 넥스트js는 정적 생성을 권고
- 정적 생성된 페이지들은 CDN에 캐시
- getStaticProps / getStaticPaths

[SSR]은 매 요청마다 html을 생성
- 항상 최신 상태 유지
- getServerSideProps
*/