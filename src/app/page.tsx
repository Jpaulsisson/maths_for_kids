'use client';
import { useEffect, useState } from 'react'
import styles from './page.module.css'
import axios from 'axios';

export default function Home() {

  useEffect(() => {
    async () => {
      const hello = await axios.get('api/hello');
      console.log(hello.data)
    }
  })

  return (
    <main>
      <h1>I'm here.</h1>
    </main>
  )
}
