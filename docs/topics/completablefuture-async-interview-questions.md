---
layout: default
title: CompletableFuture and Async Java Interview Questions and Answers
description: Java CompletableFuture interview questions covering async programming, thenApply, thenCompose, allOf, exception handling, custom thread pools, and reactive patterns.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>CompletableFuture and async interview questions.</h1>
  <p class="lede">This topic page groups CompletableFuture and asynchronous programming interview questions that test modern Java concurrency skills: composing async pipelines, handling exceptions in async chains, choosing thread pools, and understanding the reactive programming model.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/questions/19-completablefuture-and-asynchrony/' | relative_url }}">Browse CompletableFuture answers</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What this CompletableFuture section includes</h2>
  <p>CompletableFuture is Java's primary tool for non-blocking asynchronous programming. Interviewers use it to test whether candidates understand async composition (thenApply vs thenCompose), error handling (exceptionally, handle), and the implications of ForkJoinPool.commonPool() as the default executor.</p>
  <p>Strong answers demonstrate knowledge of when to use custom thread pools, how to combine multiple futures with allOf/anyOf, and how CompletableFuture compares to reactive frameworks like Project Reactor and RxJava.</p>
</section>

<section class="section">
  <h2>Representative CompletableFuture interview questions</h2>
  <ol class="topic-list">
    <li>What is CompletableFuture and how does it differ from Future?</li>
    <li>What is the difference between thenApply and thenCompose?</li>
    <li>How to handle exceptions in CompletableFuture?</li>
    <li>What is the difference between thenApply and thenApplyAsync?</li>
    <li>How does allOf work?</li>
    <li>What thread pool does CompletableFuture use by default?</li>
    <li>When should you use a custom Executor?</li>
    <li>What is the difference between supplyAsync and runAsync?</li>
    <li>How to combine results of multiple futures?</li>
    <li>How does CompletableFuture compare to reactive streams?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-concurrency-interview-questions/' | relative_url }}">Concurrency interview questions</a></h3>
      <p>CompletableFuture builds on top of Java's threading model covered in the concurrency section.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/stream-api-interview-questions/' | relative_url }}">Stream API interview questions</a></h3>
      <p>Both CompletableFuture and Stream API use functional-style composition patterns.</p>
    </article>
  </div>
</section>
