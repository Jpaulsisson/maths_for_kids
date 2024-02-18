'use client';

import { ChangeEvent, useEffect, useState } from 'react'
import styles from './page.module.css'
import axios from 'axios';
import { generateAdditionProblem } from '../utils/problems'

export default function Home() {
  const [userAnswer, setUserAnswer] = useState(0);
  const [problem, setProblem] = useState({
    x: 0,
    y: 0,
    solution: 0,
  });
  const [answerSubmitted, setAnswerSubmitted] = useState(false);

  function handleGetNewProblem() {
    const { x, y, solution } = generateAdditionProblem(2);
    setProblem({
      x,
      y,
      solution,
    })
    setUserAnswer(0);
    setAnswerSubmitted(false);
  }


  const correctAnswer = userAnswer === problem.solution;



  return (
    <main>
<h1>Clean slate</h1>
    </main>
  )
}
