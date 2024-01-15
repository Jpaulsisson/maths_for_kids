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
  const [answerCorrect, setAnswerCorrect] = useState(false);

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
      <section className={styles.titleContainer}>
        <h1>Math</h1>
        <button onClick={handleGetNewProblem} className={styles.getProblemButton}>Get a problem</button>
      </section>
      <section className={styles.problemContainer}>
        <h2>Solve:</h2>
        <p>{problem.x} + {problem.y} = {correctAnswer ? '√ Great Job!' : '?'}</p>
      </section>
      <section className={styles.solutionContainer}>
        <h2>Answer:</h2>
        <input type='text' inputMode='numeric' value={userAnswer} onChange={(e: ChangeEvent<HTMLInputElement>) => {
          setUserAnswer(Number(e.target.value))
        }} className={styles.answerInput} />
      </section>
    </main>
  )
}
