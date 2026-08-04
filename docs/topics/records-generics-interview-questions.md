---
layout: default
title: Java Records and Generics Interview Questions and Answers
description: Java Records and Generics interview questions covering Record syntax, type erasure, wildcards, bounded type parameters, PECS principle, and generic method design.
lang: en
image: /assets/social-preview/github-social-preview.png
---

<section class="hero">
  <span class="eyebrow">Topic Page</span>
  <h1>Records and Generics interview questions and answers.</h1>
  <p class="lede">This topic page groups Records and Generics interview questions that test modern Java language features: Record classes (Java 16+), type erasure mechanics, wildcards, bounded type parameters, and the PECS principle for designing generic APIs.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/questions/20-records-and-generics/' | relative_url }}">Browse Records and Generics answers</a>
    <a class="button" href="{{ '/' | relative_url }}">Back to home</a>
  </div>
</section>

<section class="section">
  <h2>What this Records and Generics section includes</h2>
  <p>Records and Generics are two distinct but important topics. Records (Java 16+) simplify immutable data class creation and are increasingly asked about in interviews. Generics test deep understanding of Java's type system: type erasure, wildcard capture, and the bridge methods the compiler generates.</p>
  <p>Strong answers cover how Record's canonical constructor works, why you cannot inherit from a Record, the difference between <code>&lt;? extends T&gt;</code> and <code>&lt;? super T&gt;</code>, and practical application of the PECS principle (Producer Extends, Consumer Super).</p>
</section>

<section class="section">
  <h2>Representative Records and Generics interview questions</h2>
  <ol class="topic-list">
    <li>What is Record in Java and since which version is it available?</li>
    <li>What are the main differences between Record and a regular class?</li>
    <li>Can you add additional methods to Record?</li>
    <li>What is a compact constructor in Record?</li>
    <li>What are Generics in Java?</li>
    <li>What is type erasure?</li>
    <li>What is the difference between <code>&lt;? extends T&gt;</code> and <code>&lt;? super T&gt;</code>?</li>
    <li>What is the PECS principle?</li>
    <li>Can you overload methods that differ only in generic parameters?</li>
    <li>Can you use multiple bounds for a single type parameter?</li>
  </ol>
</section>

<section class="section">
  <h2>Related pages</h2>
  <div class="card-grid">
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-immutability-interview-questions/' | relative_url }}">Immutability interview questions</a></h3>
      <p>Records are inherently immutable. Understanding immutability deepens your Record answers.</p>
    </article>
    <article class="card">
      <h3 class="card-title"><a href="{{ '/topics/java-collections-interview-questions/' | relative_url }}">Collections interview questions</a></h3>
      <p>Generics are fundamental to the Collections framework design.</p>
    </article>
  </div>
</section>
