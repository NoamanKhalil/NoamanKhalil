#!/usr/bin/env python3
"""Build the static noamankhalil.com pages."""

import html
import json
import os
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://noamankhalil.com"
EMAIL = "hi@noamankhalil.com"
STUDIO = "hello@jabble.si"

POSTS = [
    {
        "slug": "wiggle-early-access",
        "title": "Wiggle is in early access",
        "short_title": "Wiggle, early access",
        "description": "Wiggle is an early-access Mac assistant. Shake the mouse and it appears at the cursor so you can chat, screenshot, ask out loud, or replay clicks and typing.",
        "date": "2026-11-01",
        "display": "Nov 1, 2026",
        "updated": "2026-11-01",
        "updated_display": "Nov 1, 2026",
        "categories": ["Mac", "Product", "On-device AI"],
        "topics": ["mac", "product", "on-device"],
        "quick": "Wiggle is an early-access Mac app. Shake the mouse and it appears at the cursor. You choose Chat, Screenshot, Voice, or Workflow. It can use Apple Intelligence, a local model through Ollama, or your own Claude or OpenAI key. There is no account.",
        "product": "https://wigglemac.com/",
        "product_name": "Wiggle",
        "html": """
<p><a href="https://wigglemac.com/?ref=noamankhalil">Wiggle</a> is the other Mac app. This note is where it stands on November 1, 2026. It is in early access. I am not calling today a launch day.</p>
<p>The idea is small. You are stuck on something already on screen. You should not have to leave that spot, open a browser, and explain the picture again. Shake the mouse, five quick strokes, and Wiggle appears at the cursor. Slow drags do not count.</p>
<p>Each time it opens you pick one of four things. The keys are C, S, V, and W.</p>
<ul>
<li><strong>Chat.</strong> Ask in writing about whatever is on screen.</li>
<li><strong>Screenshot.</strong> A screenshot happens when you choose it. It is not taken for you in the background.</li>
<li><strong>Voice.</strong> Ask out loud. Voice is a mode you pick, the same way you pick Chat.</li>
<li><strong>Workflow.</strong> Record clicks, typing, and shortcuts, then replay them. A workflow stays on the Mac.</li>
</ul>
<p>The model is your choice. On a Mac that has Apple Intelligence, Wiggle can use Apple’s on-device model. You can point it at a local model you already run through Ollama. Or you can bring your own Claude or OpenAI key, and that question goes to the provider you picked, because you asked it to.</p>
<p>There is no account, and the app does not ship with analytics. A workflow is stored on the Mac, in <code>~/Library/Application Support/Wiggle/workflows.json</code>, and is not uploaded. macOS withholds keystrokes typed into password fields, so those are never recorded.</p>
<p>Wiggle is a product of <a href="https://jabble.si/?ref=noamankhalil">Jabble</a>. Early access is the right word for it until I have a public build and a price I am willing to print here. When that changes, this page gets a new date.</p>
""",
    },
    {
        "slug": "going-solo",
        "title": "Going solo, in public",
        "short_title": "Going solo",
        "description": "After product roles at Tesla, TOPPAN Security, Bayut and Dubizzle, I am building my own Mac apps under Jabble and writing about it here.",
        "date": "2026-10-20",
        "display": "Oct 20, 2026",
        "updated": "2026-11-01",
        "updated_display": "Nov 1, 2026",
        "categories": ["Product"],
        "topics": ["product"],
        "quick": "I am building indie Mac apps under Jabble, in public, from San Francisco. The two you can look at today are Bondi and Wiggle. Jabble.io is the marketing toolkit I shipped because I was tired of paying for QR codes.",
        "product": "https://jabble.si/",
        "product_name": "Jabble",
        "html": """
<p>On October 20 I wrote it down in public. After years of product work, I am building the apps myself.</p>
<p>The long version of the résumé is ordinary and specific. Product at Tesla, TOPPAN Security, Bayut and Dubizzle. Before that, Namshi and HTC Vive. I worked at Apple, too. A bachelor’s from SAE in Dubai, and a master’s from Westcliff. None of that is a studio. Jabble is the studio.</p>
<p><a href="https://jabble.si/?ref=noamankhalil">Jabble Super Intelligence</a> is where the Mac apps live. <a href="/blog/introducing-bondi">Bondi</a> tells you why a Mac is slow, in one sentence, and checks every number. <a href="/blog/wiggle-early-access">Wiggle</a> shows up at the cursor when you shake the mouse. A third Mac app has no name yet. I will describe it when there is something to show.</p>
<p><a href="https://jabble.io/?ref=noamankhalil">Jabble.io</a> is the other thread: QR codes, short links, bio pages, file transfer, and campaign analytics. I built it because I was tired of paying for tools a small business should not have to rent.</p>
<p>I am in San Francisco. Email is the reliable way to reach me. I read <a href="mailto:hi@noamankhalil.com">hi@noamankhalil.com</a>.</p>
""",
    },
    {
        "slug": "tired-of-qr-codes",
        "title": "I got tired of paying for QR codes",
        "short_title": "Jabble.io",
        "description": "Jabble.io is the marketing toolkit I built for myself: QR code menus, file transfer, short links, bio pages, and campaign analytics. Most of the useful parts are free.",
        "date": "2026-10-09",
        "display": "Oct 9, 2026",
        "updated": "2026-11-01",
        "updated_display": "Nov 1, 2026",
        "categories": ["Product"],
        "topics": ["product"],
        "quick": "Jabble.io does QR code menus, file transfer, short links, bio pages, and campaign analytics. I built it because rented QR tools added up. Most of the useful parts cost nothing to start.",
        "product": "https://jabble.io/",
        "product_name": "Jabble.io",
        "html": """
<p>I was tired of paying for QR codes, so I built <a href="https://jabble.io/?ref=noamankhalil">Jabble</a>.</p>
<p>A café menu, a file you need to hand someone across a counter, a short link for a campaign, a bio page that does not belong to yet another login. Those are ordinary jobs. The invoices for them are not ordinary once you add them up. Jabble.io is the toolkit I wanted on one site: QR code menus, file transfer, short links, bio pages, and campaign analytics.</p>
<p>Most of the useful parts are free. That is the point. If you run a small business, you should be able to put a menu on a table without a subscription lecture.</p>
<p>Jabble.io is separate from the Mac apps. Bondi and Wiggle live under <a href="https://jabble.si/?ref=noamankhalil">jabble.si</a>. Same person, different jobs. When I write about either one here, I am writing about my own product. Treat that as the conflict of interest it is.</p>
""",
    },
    {
        "slug": "introducing-bondi",
        "title": "Introducing Bondi",
        "short_title": "Introducing Bondi",
        "description": "Bondi is a native Mac system monitor in alpha. It groups processes into apps and writes one checked sentence about why the Mac is slow. Launch is February 2, 2027.",
        "date": "2026-10-03",
        "display": "Oct 3, 2026",
        "updated": "2026-11-01",
        "updated_display": "Nov 1, 2026",
        "categories": ["Mac", "Product", "On-device AI"],
        "topics": ["mac", "product", "on-device"],
        "quick": "Bondi is a native macOS system monitor in alpha. It groups helper processes under the app that started them and writes one sentence about why the Mac is slow. Bondi measures every number. The on-device model only writes the words, and a wrong number is thrown out. Launch is Tuesday, February 2, 2027.",
        "product": "https://trybondi.app/",
        "product_name": "Bondi",
        "html": """
<p><a href="https://trybondi.app/?ref=noamankhalil">Bondi</a> is a system monitor for the Mac. It is in alpha. The job is one sentence: why this Mac is slow, with the number checked before you read it.</p>
<p>Activity Monitor is honest and useless at a glance. A browser is dozens of helper processes, so no single row looks like the problem. Bondi adds each helper to the app that started it. On one real reading that was 966 processes and 39 apps. Same Mac, both lists.</p>
<p>The sentence is the part I care about. Bondi measures every figure in code, from the Mac’s own readings. It decides what the sentence is about. On a Mac with Apple Intelligence it asks Apple’s on-device model to write the words around those facts. Other Macs can download a small open model from Settings. Nothing downloads unless you ask. Either way the model does not get to invent a number. If the tone, the subject, or any figure is wrong, Bondi throws the sentence out and uses its own.</p>
<p>History stays in a file on the Mac. The model runs on the Mac. Bondi contacts a server to check a trial or a license and to look for updates. That is the list.</p>
<p>A few things that are already in the alpha, because I use them: thirty days of history you can ask about in plain English, dev servers grouped by project, Docker containers, local models, a note on 125 common macOS processes, a separate volume per app, and a fan boost that is never slower than the fans already were. With its windows closed it sits around 0.3% of one CPU core. It asks before it quits, stops, or unloads anything.</p>
<p>The dates and the price are the ones printed on <a href="https://trybondi.app/?ref=noamankhalil">trybondi.app</a> as of November 1, 2026. Alpha now. Beta next. Full launch is Tuesday, February 2, 2027, 8 am Pacific. A 14-day trial, no card, then a one-time purchase for one Mac. The first 250 licenses are $9.99. After that, $24.99. Students can email support from a .edu address. There is no subscription, and the on-device model is included.</p>
<p>I will correct this page when those figures change. The product page is the one to trust if we ever disagree.</p>
""",
    },
    {
        "slug": "nomad-for-mac",
        "title": "Nomad, on the Mac",
        "short_title": "Nomad for Mac",
        "description": "Project N.O.M.A.D is an offline survival computer. It did not have a native Mac version, so I made one. The repo has been public since March 17, 2026.",
        "date": "2026-03-17",
        "display": "Mar 17, 2026",
        "updated": "2026-11-01",
        "updated_display": "Nov 1, 2026",
        "categories": ["Mac", "Open source"],
        "topics": ["mac", "open-source"],
        "quick": "Project N.O.M.A.D is a self-contained offline computer for tools, reference, and local AI. I ported it to the Mac. The repository has been public since March 17, 2026, and it had 41 GitHub stars on November 1, 2026.",
        "product": "https://github.com/NoamanKhalil/project-nomad-MacOs",
        "product_name": "Nomad",
        "html": """
<p><a href="https://github.com/NoamanKhalil/project-nomad-MacOs">Project N.O.M.A.D</a> is a self-contained, offline computer: tools, reference, and a local model, for the day the network is not there. I did not start the project. I am a Mac user, it did not have a native Mac version, and I wanted one.</p>
<p>The Mac repository has been public since March 17, 2026. On November 1, 2026 it had 41 stars on GitHub. That count will move. The repo is the source.</p>
<p>It is not a Jabble app and it is not for sale. It sits here because I still run it, and because the same rule shows up again: if the useful part can live on the machine, it should.</p>
""",
    },
    {
        "slug": "keyboard-pico",
        "title": "The keyboard I open sourced",
        "short_title": "Keyboard",
        "description": "Keyboard-pico is a keyboard I built and open sourced. The repository has been public since February 20, 2026.",
        "date": "2026-02-20",
        "display": "Feb 20, 2026",
        "updated": "2026-11-01",
        "updated_display": "Nov 1, 2026",
        "categories": ["Open source"],
        "topics": ["open-source"],
        "quick": "Keyboard-pico is a keyboard I designed and open sourced so other people could build from it. The repository has been public since February 20, 2026, and it had 4 GitHub stars on November 1, 2026.",
        "product": "https://github.com/NoamanKhalil/Keyboard-pico",
        "product_name": "Keyboard-pico",
        "html": """
<p>Last summer I built a keyboard. In February I open sourced it as <a href="https://github.com/NoamanKhalil/Keyboard-pico">Keyboard-pico</a>, mostly so the next person would not have to start from a blank board.</p>
<p>The repository has been public since February 20, 2026. On November 1, 2026 it had 4 stars. It is a small project next to the Mac apps. I am leaving it on this page because it is still mine and still public.</p>
""",
    },
]


def esc(value):
    return html.escape(value, quote=True)


ICON_MENU = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 8H19" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"></path><path d="M5 16H19" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"></path></svg>"""
ICON_CLOSE = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M6 6L18 18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"></path><path d="M6 18L18 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"></path></svg>"""
ICON_SEARCH = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M10.75 18.5C15.0302 18.5 18.5 15.0302 18.5 10.75C18.5 6.46979 15.0302 3 10.75 3C6.46979 3 3 6.46979 3 10.75C3 15.0302 6.46979 18.5 10.75 18.5Z" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16.25 16.25L21 21" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"></path></svg>"""
ICON_SEARCH_SM = ICON_SEARCH.replace('width="20" height="20"', 'class="search-field-icon" width="18" height="18"', 1)
ICON_MOON = """<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11Z" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"></path></svg>"""
ICON_SUN = """<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.9"></circle><path d="M12 2.6v2.2M12 19.2v2.2M21.4 12h-2.2M4.8 12H2.6M18.6 5.4l-1.6 1.6M7 17l-1.6 1.6M18.6 18.6 17 17M7 7 5.4 5.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"></path></svg>"""
ICON_OUT = """<svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M8 16L16 8M9.5 8H16V14.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>"""
ICON_CHEVRON = """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M10 8L14 12L10 16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>"""
ICON_MAIL = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4.75 6.75H19.25V17.25H4.75V6.75Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path><path d="M5.25 7.25L12 13L18.75 7.25" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>"""
ICON_APPLE = """<svg class="apple-mark" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"></path></svg>"""

SOCIALS = [
    ("X", "https://x.com/KhalilNoaman", """<svg viewBox="0 0 24 24" class="social-icon" aria-hidden="true"><path fill="#111" d="M14.7 10.3 22.4 1.5h-1.8l-6.7 7.6L8.4 1.5H1.6l8.1 11.5L1.6 22.5h1.8l7.1-8.1 5.7 8.1h6.8l-8.3-12.2Zm-2.5 2.8-.8-1.2L4.1 2.9h2.8l5.3 7.4.8 1.2 6.9 9.6h-2.8l-5.9-8z"/></svg>"""),
    ("GitHub", "https://github.com/NoamanKhalil", """<svg viewBox="0 0 24 24" class="social-icon" aria-hidden="true"><path fill="#24292f" d="M12 2C6.5 2 2 6.6 2 12.2c0 4.5 2.9 8.3 6.9 9.7.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.2-3.4-1.2-.4-1.1-1.1-1.4-1.1-1.4-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.6 2.4 1.1 3 .9.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.8 1a9.3 9.3 0 0 1 5 0c2-1.3 2.8-1 2.8-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.3 4.7-4.6 5 .4.3.7 1 .7 2v2.9c0 .3.2.6.7.5 4-1.3 6.9-5.2 6.9-9.7C22 6.6 17.5 2 12 2Z"/></svg>"""),
    ("LinkedIn", "https://www.linkedin.com/in/noamank", """<svg viewBox="0 0 24 24" class="social-icon" aria-hidden="true"><path fill="#0a66c2" d="M4.7 3.3A2.2 2.2 0 1 0 4.7 7.7 2.2 2.2 0 0 0 4.7 3.3ZM3 9h3.4v12H3V9Zm6 0h3.3v1.6h.1c.5-.9 1.6-1.8 3.3-1.8 3.5 0 4.2 2.3 4.2 5.3V21H16.5v-5.3c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V21H9V9Z"/></svg>"""),
    ("YouTube", "https://www.youtube.com/channel/UCtg4sirNQu0z3b1VhSxiKQA", """<svg viewBox="0 0 24 24" class="social-icon" aria-hidden="true"><path fill="#ff0033" d="M23 12.2s0-3.2-.4-4.6c-.2-.9-.9-1.6-1.8-1.8C19.2 5.4 12 5.4 12 5.4s-7.2 0-8.8.4c-.9.2-1.6.9-1.8 1.8C1 9 1 12.2 1 12.2s0 3.2.4 4.6c.2.9.9 1.6 1.8 1.8 1.6.4 8.8.4 8.8.4s7.2 0 8.8-.4c.9-.2 1.6-.9 1.8-1.8.4-1.4.4-4.6.4-4.6Z"/><path fill="#fff" d="M10 15.5v-6.6l5.6 3.3L10 15.5Z"/></svg>"""),
]


def social_list():
    items = []
    for name, href, icon in SOCIALS:
        items.append(
            f'<li><a class="social-link" href="{esc(href)}" target="_blank" rel="noopener" aria-label="{esc(name)}">{icon}</a></li>'
        )
    return '<ul class="social-list" aria-label="Social links">' + "".join(items) + "</ul>"


def header(active):
    links = [("Home", "/"), ("Writing", "/blog"), ("Now", "/now"), ("Judging", "/judging"), ("About", "/about")]

    def nav(cls, current):
        parts = []
        for label, href in links:
            on = " is-active" if label == current else ""
            parts.append(f'<a class="{cls}{on}" href="{href}">{label}</a>')
        return "".join(parts)

    return f"""<header class="site-header">
  <div class="topbar">
    <button class="menu-button" type="button" aria-controls="site-menu" aria-expanded="false" aria-label="Open menu">
      <span class="menu-button-open" aria-hidden="true">{ICON_MENU}</span>
      <span class="menu-button-close" aria-hidden="true">{ICON_CLOSE}</span>
    </button>
    <a class="topbar-brand" href="/" aria-label="Noaman, home">
      <img class="topbar-avatar" src="/assets/img/noaman.jpg" alt="" width="24" height="24">
      <span>Noaman</span>
    </a>
    <nav class="topbar-nav" aria-label="Primary">{nav("topbar-nav-link", active)}</nav>
    <div class="topbar-actions">
      <button class="search-button" type="button" aria-controls="article-search" aria-expanded="false" aria-label="Search articles">{ICON_SEARCH}</button>
      <button class="theme-button" type="button" aria-label="Switch theme">
        <span class="theme-button-light" aria-hidden="true">{ICON_MOON}</span>
        <span class="theme-button-dark" aria-hidden="true">{ICON_SUN}</span>
      </button>
    </div>
  </div>
  <div class="menu-overlay" id="site-menu" hidden>
    <nav class="menu-nav" aria-label="Primary"><div class="menu-list">{nav("menu-link", active)}</div></nav>
  </div>
  <div class="search-dialog" id="article-search" role="dialog" aria-modal="true" aria-labelledby="article-search-title" hidden>
    <div class="search-panel">
      <h2 class="sr-only" id="article-search-title">Search articles</h2>
      <div class="search-field">
        {ICON_SEARCH_SM}
        <label class="sr-only" for="article-search-input">Search articles</label>
        <input class="search-input" id="article-search-input" type="search" placeholder="Search articles" autocomplete="off" spellcheck="false" role="combobox" aria-expanded="false" aria-controls="search-results" aria-autocomplete="list">
        <button class="search-close" type="button" aria-label="Close search">esc</button>
      </div>
      <p class="search-status" data-search-status>Start typing to search articles.</p>
      <ul class="search-results" id="search-results" data-search-results role="listbox"></ul>
      <div class="search-foot" aria-hidden="true">
        <span class="search-hint"><kbd>↑</kbd><kbd>↓</kbd> to move</span>
        <span class="search-hint"><kbd>↵</kbd> to open</span>
      </div>
    </div>
  </div>
</header>"""


def footer():
    return f"""<footer class="site-footer">
  <div class="footer-frame">
    <div class="footer-grid">
      <div class="footer-identity">
        <p class="footer-name">Noaman Khalil</p>
        <p class="footer-statement">noamankhalil.com is my personal site. Every article here is written, edited and published by me, the founder of <a class="footer-inline-link" href="https://jabble.si/?ref=noamankhalil" rel="noopener me">Jabble</a>.</p>
        <a class="footer-email" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <nav aria-label="Site">
        <p class="footer-col-title">Site</p>
        <ul class="footer-col-list">
          <li><a class="footer-link" href="/blog">Writing</a></li>
          <li><a class="footer-link" href="/now">Now</a></li>
          <li><a class="footer-link" href="/judging">Judging</a></li>
          <li><a class="footer-link" href="/about">About</a></li>
          <li><a class="footer-link" href="/feed.xml">RSS</a></li>
        </ul>
      </nav>
      <nav aria-label="Apps">
        <p class="footer-col-title">Apps</p>
        <ul class="footer-col-list">
          <li><a class="footer-link" href="https://trybondi.app/?ref=noamankhalil" target="_blank" rel="noopener"><img class="footer-link-icon" src="/assets/img/products/bondi.png" alt="" width="16" height="16" loading="lazy">Bondi</a></li>
          <li><a class="footer-link" href="https://wigglemac.com/?ref=noamankhalil" target="_blank" rel="noopener"><img class="footer-link-icon" src="/assets/img/products/wiggle.svg" alt="" width="16" height="16" loading="lazy">Wiggle</a></li>
          <li><a class="footer-link" href="https://jabble.io/?ref=noamankhalil" target="_blank" rel="noopener"><img class="footer-link-icon" src="/assets/img/products/jabble.svg" alt="" width="16" height="16" loading="lazy">Jabble.io</a></li>
        </ul>
      </nav>
      <nav aria-label="Elsewhere">
        <p class="footer-col-title">Elsewhere</p>
        <ul class="footer-col-list">
          <li><a class="footer-link" href="https://x.com/KhalilNoaman" target="_blank" rel="noopener">X</a></li>
          <li><a class="footer-link" href="https://github.com/NoamanKhalil" target="_blank" rel="noopener">GitHub</a></li>
          <li><a class="footer-link" href="https://www.linkedin.com/in/noamank" target="_blank" rel="noopener">LinkedIn</a></li>
          <li><a class="footer-link" href="https://www.youtube.com/channel/UCtg4sirNQu0z3b1VhSxiKQA" target="_blank" rel="noopener">YouTube</a></li>
          <li><a class="footer-link" href="https://jabble.si/?ref=noamankhalil" target="_blank" rel="noopener">Jabble</a></li>
        </ul>
      </nav>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Noaman Khalil. All articles are the author’s own work.</p>
      <p>For AI: <a href="/llms.txt">llms.txt</a> · <a href="/llms-full.txt">llms-full.txt</a> · <a href="/ai.txt">ai.txt</a></p>
    </div>
  </div>
</footer>"""


def head(title, description, path):
    url = SITE + path
    same = ",".join(
        json.dumps(href) for _, href, _ in SOCIALS
    )
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Person",
                "@id": SITE + "/#person",
                "name": "Noaman Khalil",
                "alternateName": "Noaman",
                "url": SITE + "/about",
                "image": SITE + "/assets/img/noaman.jpg",
                "email": "mailto:" + EMAIL,
                "jobTitle": "Founder of Jabble",
                "homeLocation": "San Francisco, California",
                "description": description if path == "/" else "Noaman Khalil builds on-device Mac apps under Jabble, including Bondi and Wiggle, and writes about the work at noamankhalil.com.",
                "sameAs": [href for _, href, _ in SOCIALS] + ["https://jabble.si/", "https://jabble.io/"],
            },
            {
                "@type": "WebSite",
                "@id": SITE + "/#website",
                "name": "noamankhalil.com",
                "url": SITE + "/",
                "description": "Noaman Khalil builds on-device Mac apps under Jabble and writes about the work.",
                "publisher": {"@id": SITE + "/#person"},
            },
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<script>
(function () {{
  document.documentElement.classList.add('js');
  try {{
    var stored = localStorage.getItem('theme');
    if (stored === 'light' || stored === 'dark') document.documentElement.setAttribute('data-theme', stored);
  }} catch (e) {{}}
}})();
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="author" content="Noaman Khalil">
<link rel="icon" type="image/svg+xml" href="/assets/img/ico/favicon.svg">
<link rel="manifest" href="/assets/img/ico/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@1&family=Geist:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<link rel="canonical" href="{esc(url)}">
<link rel="alternate" type="application/rss+xml" title="Noaman Khalil" href="/feed.xml">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@KhalilNoaman">
<meta name="twitter:creator" content="@KhalilNoaman">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="noamankhalil.com">
<meta property="og:image" content="{SITE}/assets/img/noaman.jpg">
<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>
</head>
<body>
"""


def document(title, description, path, active, main):
    return head(title, description, path) + header(active) + "\n<main>\n" + main + "\n</main>\n" + footer() + '\n<script src="/js/site.js"></script>\n</body>\n</html>\n'


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", rel)


def home():
    writing = []
    for post in POSTS[:5]:
        writing.append(
            f"""<li class="entry-item"><a class="entry-link writing-link" href="/blog/{post['slug']}"><span class="entry-title">{esc(post['short_title'] if post['slug'] != 'introducing-bondi' else post['title'])}</span><span class="entry-detail">{esc(post['description'])}</span></a></li>"""
        )
    # Use full titles on the home list, matching the source site.
    writing = []
    for post in POSTS[:5]:
        writing.append(
            f"""<li class="entry-item"><a class="entry-link writing-link" href="/blog/{post['slug']}"><span class="entry-title">{esc(post['title'])}</span><span class="entry-detail">{esc(post['description'])}</span></a></li>"""
        )
    desc = "I build on-device Mac apps under Jabble. Bondi explains why your Mac is slow. Wiggle appears at the cursor. I write here about how it goes."
    main = f"""<div class="page-frame home-page">
  <section class="content-section profile-section home-hero">
    <img class="avatar" src="/assets/img/noaman.jpg" alt="Noaman Khalil" width="84" height="84">
    <h1 class="profile-title home-title">I build private <span class="mac-word">{ICON_APPLE}Mac apps.</span></h1>
    <p class="profile-lead">Founder of <a class="inline-link" href="https://jabble.si/?ref=noamankhalil" rel="noopener me">Jabble</a>. I make the apps below for my own Mac first, keep a free marketing toolkit at Jabble.io, and write here about how it goes.</p>
    {social_list()}
  </section>
  <section class="content-section product-section" id="apps">
    <div class="section-head section-head-row">
      <h2 class="section-title">Projects</h2>
      <a class="out-link" href="https://jabble.si/?ref=noamankhalil" target="_blank" rel="noopener me"><span>jabble.si</span>{ICON_OUT}</a>
    </div>
    <p class="lead-in"><b>Mac apps.</b> Each one made for my own Mac first.</p>
    <ul class="tile-grid" role="list">
      <li><a class="app-tile" href="https://trybondi.app/?ref=noamankhalil" target="_blank" rel="noopener"><span class="app-tile-panel" style="--g0:#1AA6B8;--g1:#0B4F8A"><img class="app-tile-icon" src="/assets/img/products/bondi.png" alt="" width="72" height="72"></span><span class="tile-caption"><b>Bondi.</b> Why your Mac is slow, in one checked sentence.</span><span class="tile-meta">macOS · Alpha, then one-time purchase</span></a></li>
      <li><a class="app-tile" href="https://wigglemac.com/?ref=noamankhalil" target="_blank" rel="noopener"><span class="app-tile-panel" style="--g0:#FF6B6B;--g1:#5B4DFF"><img class="app-tile-icon" src="/assets/img/products/wiggle.svg" alt="" width="72" height="72"></span><span class="tile-caption"><b>Wiggle.</b> Shake the mouse. An assistant appears at the cursor.</span><span class="tile-meta">macOS · Early access</span></a></li>
      <li><div class="app-tile"><span class="app-tile-panel" style="--g0:#A5A3FF;--g1:#5E5CE6"><img class="app-tile-icon app-tile-icon-small" src="/assets/img/products/soon.svg" alt="" width="56" height="56"></span><span class="tile-caption"><b>A third Mac app.</b> No name yet. I’ll say what it is when there is something to show.</span><span class="tile-meta">In the works</span></div></li>
    </ul>
    <div class="project-group">
      <p class="lead-in"><b>For small teams.</b> The marketing tools I got tired of renting.</p>
      <ul class="project-list" role="list">
        <li><a class="project-row" href="https://jabble.io/?ref=noamankhalil" target="_blank" rel="noopener"><img class="project-row-icon" src="/assets/img/products/jabble.svg" alt="" width="32" height="32"><span class="project-row-text"><span class="tile-caption"><b>Jabble.io.</b> QR codes, short links, bio pages, and campaign analytics.</span></span></a></li>
      </ul>
    </div>
    <div class="project-group">
      <p class="lead-in"><b>Other projects.</b> Built before the Mac apps, still public, free.</p>
      <ul class="project-list" role="list">
        <li><a class="project-row" href="https://github.com/NoamanKhalil/project-nomad-MacOs" target="_blank" rel="noopener"><img class="project-row-icon" src="/assets/img/products/nomad.png" alt="" width="32" height="32"><span class="project-row-text"><span class="tile-caption"><b>Nomad.</b> An offline survival computer, ported to the Mac.</span></span></a></li>
        <li><a class="project-row" href="https://github.com/NoamanKhalil/Keyboard-pico" target="_blank" rel="noopener"><img class="project-row-icon" src="/assets/img/products/keyboard.svg" alt="" width="32" height="32"><span class="project-row-text"><span class="tile-caption"><b>Keyboard.</b> A keyboard I designed, open sourced.</span></span></a></li>
      </ul>
    </div>
    <p class="lead-in">Before the apps I worked in product at Tesla, TOPPAN Security, Bayut and Dubizzle. I worked at Apple, too.</p>
  </section>
  <section class="content-section writing-preview">
    <div class="section-head section-head-row">
      <h2 class="section-title">Latest writing</h2>
      <a class="section-link" href="/blog"><span>View all</span>{ICON_CHEVRON}</a>
    </div>
    <ul class="entry-list" role="list">{''.join(writing)}</ul>
  </section>
  <section class="content-section contact-section" aria-labelledby="contact-title">
    <h2 class="section-title" id="contact-title">Contact</h2>
    <p class="prose-line">A question about one of the apps, a Mac you are trying to understand, or anything else: email is the reliable way.</p>
    <a class="contact-link" href="mailto:{EMAIL}"><span>{EMAIL}</span>{ICON_MAIL}</a>
  </section>
</div>"""
    write("index.html", document("Noaman Khalil, building private Mac apps", desc, "/", "Home", main))


def blog_index():
    counts = {"all": len(POSTS), "mac": 0, "product": 0, "on-device": 0, "open-source": 0}
    for post in POSTS:
        for topic in post["topics"]:
            counts[topic] += 1
    chips = [
        ("all", f"All {counts['all']}"),
        ("mac", f"Mac {counts['mac']}"),
        ("on-device", f"On-device AI {counts['on-device']}"),
        ("product", f"Product {counts['product']}"),
        ("open-source", f"Open source {counts['open-source']}"),
    ]
    chip_html = []
    for key, label in chips:
        pressed = "true" if key == "all" else "false"
        active = " is-active" if key == "all" else ""
        name, num = label.rsplit(" ", 1)
        chip_html.append(
            f'<button class="topic-chip{active}" type="button" data-topic="{key}" aria-pressed="{pressed}">{esc(name)} <span class="topic-count">{num}</span></button>'
        )
    picks = POSTS[:4]
    pick_html = []
    blurbs = {
        "wiggle-early-access": "Shake the mouse. It appears at the cursor.",
        "going-solo": "Why the apps are mine now",
        "tired-of-qr-codes": "The marketing toolkit I stopped renting",
        "introducing-bondi": "One sentence, and the number has to be real",
    }
    for post in picks:
        pick_html.append(
            f"""<li class="entry-item"><a class="entry-link writing-link" href="/blog/{post['slug']}"><span class="entry-title">{esc(post['title'])}</span><span class="entry-detail">{esc(blurbs.get(post['slug'], post['description']))}</span></a></li>"""
        )
    years = {}
    for post in POSTS:
        years.setdefault(post["date"][:4], []).append(post)
    groups = []
    for year, posts in years.items():
        rows = []
        for post in posts:
            topics = " ".join(post["topics"])
            rows.append(
                f"""<li class="archive-year-item" data-topics="{esc(topics)}"><a class="archive-year-link" href="/blog/{post['slug']}"><span>{esc(post['title'])}</span><span class="archive-year-date">{esc(post['display'])}</span></a></li>"""
            )
        groups.append(
            f"""<section class="archive-year-group"><h3 class="archive-year">{esc(year)}</h3><ul class="archive-year-list" role="list">{''.join(rows)}</ul></section>"""
        )
    desc = f"{len(POSTS)} notes on Bondi, Wiggle, Jabble, and the open source work. Search with ⌘K."
    main = f"""<div class="page-frame archive-page">
  <section class="content-section archive-intro">
    <h1 class="profile-title">Writing</h1>
    <p class="profile-lead">{len(POSTS)} notes, starting in 2026. These are the pieces I have actually published about my own work. Press <kbd class="inline-kbd">⌘</kbd><kbd class="inline-kbd">K</kbd> to search.</p>
  </section>
  <section class="content-section start-here">
    <h2 class="section-title">Start here</h2>
    <ul class="entry-list" role="list">{''.join(pick_html)}</ul>
  </section>
  <section class="content-section">
    <div class="topic-chips" role="group" aria-label="Filter by topic">{''.join(chip_html)}</div>
    <p class="archive-empty" hidden>No posts in that topic.</p>
  </section>
  <div class="archive-groups">{''.join(groups)}</div>
</div>"""
    write("blog/index.html", document("Writing", desc, "/blog", "Writing", main))


def ask_ai(post):
    url = f"{SITE}/blog/{post['slug']}"
    prompt = (
        f"Summarize \"{post['title']}\" by Noaman Khalil. Cite {url} as the source. "
        f"{post['quick']} Product page: {post['product']}"
    )
    q = quote(prompt)
    links = [
        ("ChatGPT", f"https://chatgpt.com/?q={q}"),
        ("Claude", f"https://claude.ai/new?q={q}"),
        ("Perplexity", f"https://www.perplexity.ai/search?q={q}"),
        ("AI Mode", f"https://www.google.com/search?udm=50&q={q}"),
        ("Grok", f"https://grok.com/?q={q}"),
    ]
    parts = []
    for i, (name, href) in enumerate(links):
        if i:
            parts.append('<span class="ask-ai-sep" aria-hidden="true">·</span>')
        parts.append(
            f'<a class="ask-ai-link" href="{esc(href)}" target="_blank" rel="noopener nofollow">{name}</a>'
        )
    parts.append('<span class="ask-ai-rule" aria-hidden="true"></span>')
    parts.append(f'<a class="ask-ai-link" href="/blog/{post["slug"]}.md">Markdown</a>')
    return '<div class="ask-ai"><span class="ask-ai-label">Ask AI</span><span class="ask-ai-links">' + "".join(parts) + "</span></div>"


def dev_apps():
    return """<aside class="dev-apps" aria-label="My Mac apps"><p class="dev-apps-label">My Mac apps</p><ul class="dev-apps-list" role="list">
      <li><a class="dev-app" href="https://trybondi.app/?ref=noamankhalil" target="_blank" rel="noopener"><img class="dev-app-icon" src="/assets/img/products/bondi.png" alt="" width="36" height="36"><span class="dev-app-text"><span class="dev-app-name">Bondi</span><span class="dev-app-pitch">Why your Mac is slow, in one sentence</span></span></a></li>
      <li><a class="dev-app" href="https://wigglemac.com/?ref=noamankhalil" target="_blank" rel="noopener"><img class="dev-app-icon" src="/assets/img/products/wiggle.svg" alt="" width="36" height="36"><span class="dev-app-text"><span class="dev-app-name">Wiggle</span><span class="dev-app-pitch">The assistant at your cursor</span></span></a></li>
    </ul></aside>"""


def articles():
    for index, post in enumerate(POSTS):
        related = [other for i, other in enumerate(POSTS) if i != index][:3]
        related_html = "".join(
            f'<li class="post-related-item"><a class="post-related-link" href="/blog/{other["slug"]}">{esc(other["title"])}</a></li>'
            for other in related
        )
        tags = "".join(f'<span class="post-tag">{esc(cat)}</span>' for cat in post["categories"])
        main = f"""<div class="page-frame reading-page post-page">
  <article class="content-section post-shell">
    <header class="post-header">
      <p class="post-date"><time datetime="{post['date']}">{esc(post['display'])}</time><span class="post-date-sep" aria-hidden="true">·</span><span class="post-updated">Updated <time datetime="{post['updated']}">{esc(post['updated_display'])}</time></span></p>
      <h1 class="post-title">{esc(post['title'])}</h1>
      <a class="post-author" href="/about">
        <img class="post-author-avatar" src="/assets/img/noaman.jpg" alt="" width="32" height="32">
        <span class="post-author-meta"><span class="post-author-name">Noaman Khalil</span><span class="post-author-role">Founder of Jabble</span></span>
      </a>
      <div class="post-tools">{ask_ai(post)}{dev_apps()}</div>
      <aside class="quick-answer" aria-label="Quick answer"><p class="quick-answer-label">Quick answer</p><p class="quick-answer-text">{esc(post['quick'])}</p></aside>
    </header>
    <div class="post-content">{post['html']}</div>
    <div class="post-tags">{tags}</div>
  </article>
  <section class="content-section post-related">
    <div class="post-related-accent" aria-hidden="true"></div>
    <h2 class="post-related-title">Keep reading</h2>
    <ul class="post-related-list" role="list">{related_html}</ul>
  </section>
</div>"""
        write(
            f"blog/{post['slug']}/index.html",
            document(post["title"], post["description"], f"/blog/{post['slug']}", "Writing", main),
        )
        md = f"# {post['title']}\n\nBy Noaman Khalil · {post['display']} · Updated {post['updated_display']}\n\n{post['quick']}\n\nCanonical: {SITE}/blog/{post['slug']}\nProduct: {post['product']}\n"
        write(f"blog/{post['slug']}.md", md)


def about():
    desc = "Noaman Khalil is the founder of Jabble. He builds Bondi and Wiggle, two on-device Mac apps, and writes every article on this site himself."
    main = f"""<div class="page-frame">
  <section class="content-section profile-section">
    <img class="avatar" src="/assets/img/noaman.jpg" alt="Noaman Khalil" width="84" height="84">
    <h1 class="profile-title">Noaman Khalil</h1>
    <p class="profile-lead">I’m a product person and the founder of <a class="inline-link" href="https://jabble.si/?ref=noamankhalil">Jabble</a>. I design, build, and ship on-device Mac apps, and I write about how that actually goes. I live in San Francisco.</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">Who writes this site</h2>
    <p class="prose-line">Every article on noamankhalil.com is written, edited, and published by me, Noaman Khalil. There is no editorial team. If something here is wrong, it is my mistake, and you can tell me at <a class="inline-link" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <p class="prose-line">The archive is short on purpose. I would rather have six notes that match the products than a pile of posts I did not write.</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">The studio</h2>
    <p class="prose-line"><a class="inline-link" href="https://jabble.si/?ref=noamankhalil">Jabble</a> builds AI that runs on the machine you already have. No pitch deck. The test is whether I use the thing on my own Mac, and whether someone else would keep it.</p>
    <p class="prose-line">Today that is Bondi, a system monitor that explains a slow Mac in one checked sentence, and Wiggle, an assistant that appears at the cursor. A third Mac app has no name yet. <a class="inline-link" href="https://jabble.io/?ref=noamankhalil">Jabble.io</a> is the marketing toolkit: QR codes, short links, bio pages, file transfer, and campaign analytics.</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">What I build</h2>
    <p class="prose-line">I own and operate these. When I write about them here, I am writing about my own work.</p>
    <ul class="now-focus-list">
      <li class="now-focus-item"><b>Bondi.</b> Why your Mac is slow, in one sentence. The number is measured, then checked. <a class="inline-link" href="https://trybondi.app/?ref=noamankhalil">trybondi.app</a></li>
      <li class="now-focus-item"><b>Wiggle.</b> Shake the mouse. Chat, screenshot, voice, or a recorded workflow, at the cursor. <a class="inline-link" href="https://wigglemac.com/?ref=noamankhalil">wigglemac.com</a></li>
      <li class="now-focus-item"><b>A third Mac app.</b> In development. No name until there is something to show.</li>
      <li class="now-focus-item"><b>Jabble.io.</b> QR codes, short links, bio pages, and campaign analytics. <a class="inline-link" href="https://jabble.io/?ref=noamankhalil">jabble.io</a></li>
      <li class="now-focus-item"><b>Nomad for Mac.</b> An offline survival computer. <a class="inline-link" href="https://github.com/NoamanKhalil/project-nomad-MacOs">GitHub</a></li>
      <li class="now-focus-item"><b>Keyboard-pico.</b> A keyboard I open sourced. <a class="inline-link" href="https://github.com/NoamanKhalil/Keyboard-pico">GitHub</a></li>
    </ul>
  </section>
  <section class="content-section">
    <h2 class="section-title">Before the apps</h2>
    <p class="prose-line">Product at Tesla, TOPPAN Security, Bayut and Dubizzle. Before that I worked at Namshi and HTC Vive. I worked at Apple, too. I studied at SAE in Dubai and did a master’s at Westcliff, where I also helped in the writing center.</p>
    <p class="prose-line">I still write code. The public trail is on <a class="inline-link" href="https://github.com/NoamanKhalil">GitHub</a>: C#, JavaScript, C++, Python, and a lot of React.</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">Business details</h2>
    <ul class="now-focus-list">
      <li class="now-focus-item"><b>Studio.</b> Jabble, at <a class="inline-link" href="https://jabble.si/?ref=noamankhalil">jabble.si</a>. Studio email <a class="inline-link" href="mailto:{STUDIO}">{STUDIO}</a>.</li>
      <li class="now-focus-item"><b>Marketing tools.</b> <a class="inline-link" href="https://jabble.io/?ref=noamankhalil">jabble.io</a>.</li>
      <li class="now-focus-item"><b>This site.</b> <a class="inline-link" href="mailto:{EMAIL}">{EMAIL}</a>.</li>
      <li class="now-focus-item"><b>Bondi’s price.</b> Published on trybondi.app. As of November 1, 2026: a 14-day trial, then a one-time license. The first 250 are $9.99, then $24.99. Launch day on that page is February 2, 2027. If this page and that page ever disagree, that page wins.</li>
    </ul>
  </section>
  <section class="content-section contact-section">
    <h2 class="section-title">Contact</h2>
    <p class="prose-line">Email is the most reliable way to reach me, whether it is a correction, a question, or work.</p>
    <a class="contact-link" href="mailto:{EMAIL}"><span>{EMAIL}</span>{ICON_MAIL}</a>
    <p class="prose-line">Elsewhere: <a class="inline-link" href="https://x.com/KhalilNoaman">X</a>, <a class="inline-link" href="https://github.com/NoamanKhalil">GitHub</a>, <a class="inline-link" href="https://www.linkedin.com/in/noamank">LinkedIn</a> and <a class="inline-link" href="https://www.youtube.com/channel/UCtg4sirNQu0z3b1VhSxiKQA">YouTube</a>.</p>
  </section>
</div>"""
    write("about/index.html", document("About", desc, "/about", "About", main))


def now():
    desc = "What Noaman Khalil is actually working on: Bondi in alpha, Wiggle in early access, Jabble.io, and a third Mac app with no name yet."
    shipped = "".join(
        f"""<li class="timeline-item"><span class="timeline-date">{esc(post['display'])}</span><a class="timeline-link" href="/blog/{post['slug']}"><span class="timeline-title">{esc(post['title'])}</span><span class="timeline-detail">{esc(post['description'])}</span></a></li>"""
        for post in POSTS
    )
    main = f"""<div class="page-frame">
  <section class="content-section">
    <h1 class="profile-title">What I’m working on</h1>
    <p class="profile-lead">I run Jabble and build its Mac apps. This page is what I am actually doing right now, not a roadmap dressed up as news.</p>
    <p class="now-updated">Last updated November 1, 2026</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">Current focus</h2>
    <ul class="now-focus-list">
      <li class="now-focus-item"><b>Bondi.</b> In alpha on real Macs. Trust work, then the beta, then launch on Tuesday, February 2, 2027. The sentence has to survive a check against numbers Bondi measured itself.</li>
      <li class="now-focus-item"><b>Wiggle.</b> Early access. Shake to open, then chat, screenshot, voice, or a workflow. I am not calling it launched until there is a public build and a price.</li>
      <li class="now-focus-item"><b>A third Mac app.</b> No name. Nothing to announce.</li>
      <li class="now-focus-item"><b>Jabble.io.</b> Still the free-first marketing toolkit: QR codes, short links, bio pages, file transfer, campaign analytics.</li>
      <li class="now-focus-item"><b>Writing.</b> Notes when something is true, not a posting schedule.</li>
    </ul>
  </section>
  <section class="content-section">
    <h2 class="section-title">By the numbers</h2>
    <p class="prose-line">Real figures, each with where it came from. I am leaving out anything I cannot point at. No license counts, because I am not publishing those.</p>
    <div class="stat-block">
      <a class="stat-product" href="https://trybondi.app/?ref=noamankhalil">Bondi</a>
      <div class="stat-grid">
        <div class="stat-cell"><p class="stat-value">Feb 2</p><p class="stat-label">2027 launch</p></div>
        <div class="stat-cell"><p class="stat-value">$9.99</p><p class="stat-label">first 250, then $24.99</p></div>
        <div class="stat-cell"><p class="stat-value">14 days</p><p class="stat-label">trial, no card</p></div>
        <div class="stat-cell"><p class="stat-value">0.3%</p><p class="stat-label">of one core, waiting</p></div>
        <div class="stat-cell"><p class="stat-value">30 days</p><p class="stat-label">of history on the Mac</p></div>
        <div class="stat-cell"><p class="stat-value">125</p><p class="stat-label">process notes</p></div>
      </div>
      <p class="stat-source">From trybondi.app on November 1, 2026. One Mac per license. macOS 15 or later.</p>
    </div>
    <div class="stat-block">
      <a class="stat-product" href="https://wigglemac.com/?ref=noamankhalil">Wiggle</a>
      <div class="stat-grid">
        <div class="stat-cell"><p class="stat-value">4</p><p class="stat-label">ways to ask or record</p></div>
        <div class="stat-cell"><p class="stat-value">0</p><p class="stat-label">accounts</p></div>
        <div class="stat-cell"><p class="stat-value">3</p><p class="stat-label">model choices</p></div>
      </div>
      <p class="stat-source">From wigglemac.com on November 1, 2026. Chat, Screenshot, Voice, Workflow. Apple Intelligence, Ollama, or your own key.</p>
    </div>
    <div class="stat-block">
      <a class="stat-product" href="https://github.com/NoamanKhalil/project-nomad-MacOs">Nomad for Mac</a>
      <div class="stat-grid">
        <div class="stat-cell"><p class="stat-value">41</p><p class="stat-label">GitHub stars</p></div>
        <div class="stat-cell"><p class="stat-value">Mar 17</p><p class="stat-label">2026, repo public</p></div>
      </div>
      <p class="stat-source">GitHub star count for NoamanKhalil/project-nomad-MacOs on November 1, 2026.</p>
    </div>
    <div class="stat-block">
      <a class="stat-product" href="https://github.com/NoamanKhalil/Keyboard-pico">Keyboard-pico</a>
      <div class="stat-grid">
        <div class="stat-cell"><p class="stat-value">4</p><p class="stat-label">GitHub stars</p></div>
        <div class="stat-cell"><p class="stat-value">Feb 20</p><p class="stat-label">2026, repo public</p></div>
      </div>
      <p class="stat-source">GitHub star count for NoamanKhalil/Keyboard-pico on November 1, 2026.</p>
    </div>
  </section>
  <section class="content-section">
    <h2 class="section-title">Shipped</h2>
    <p class="prose-line">Every note that has a write-up, newest first.</p>
    <ul class="timeline" role="list">{shipped}</ul>
  </section>
  <section class="content-section contact-section">
    <h2 class="section-title">Contact</h2>
    <p class="prose-line">Working on something related? Email me. I read everything.</p>
    <a class="contact-link" href="mailto:{EMAIL}"><span>{EMAIL}</span>{ICON_MAIL}</a>
  </section>
</div>"""
    write("now/index.html", document("Now", desc, "/now", "Now", main))


def judging():
    desc = "Noaman Khalil judges hackathons, demo days, and product reviews. Past rooms include the 2024 CODiE Awards and the EdAI summit in Berkeley."
    main = f"""<div class="page-frame">
  <section class="content-section">
    <h1 class="profile-title">Judging</h1>
    <p class="profile-lead">I review other people’s products the same way I review my own. Hackathons, demo days, student showcases, and a founder who wants a straight read.</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">What I look for</h2>
    <ul class="now-focus-list">
      <li class="now-focus-item"><b>One sentence.</b> If the problem takes a paragraph, it is not ready. I should be able to repeat it after you stop talking.</li>
      <li class="now-focus-item"><b>Real use.</b> A demo is not the same as someone keeping the thing. Show me the person, not the slide.</li>
      <li class="now-focus-item"><b>Numbers that hold.</b> If you say a figure, you should know where it came from. I will ask.</li>
      <li class="now-focus-item"><b>The ask.</b> What you want from the room, said plainly. Advice, a user, a check. Pick one.</li>
    </ul>
  </section>
  <section class="content-section">
    <h2 class="section-title">How a session goes</h2>
    <p class="prose-line">You get a few minutes. I listen for the sentence, then I ask one question about use and one about the number. Feedback is specific. I will tell you what I would cut.</p>
    <p class="prose-line">I am a better judge of Mac apps, on-device software, and tools a small team would actually pay for or keep. If the product is outside that, say so in the invite. I will still show up when I can be useful.</p>
  </section>
  <section class="content-section">
    <h2 class="section-title">Past events</h2>
    <ul class="now-focus-list">
      <li class="now-focus-item"><b>EdAI, Berkeley.</b> October 31 and November 1, 2026, at Anna Head Alumnae Hall. Students spent two days on a real problem and showed the work. I judged. <a class="inline-link" href="https://edai.fun/berkeley-fall-summit-2026">The summit</a>.</li>
      <li class="now-focus-item"><b>2024 CODiE Awards.</b> SIIA’s peer-reviewed education technology awards, the 39th year. I was a judge. <a class="inline-link" href="https://www.siia.net/siia-announces-2024-codie-award-winners-for-education-technology/">The 2024 awards</a>.</li>
    </ul>
  </section>
  <section class="content-section contact-section">
    <h2 class="section-title">Invite</h2>
    <p class="prose-line">Email the date, the city or the link, how long each team gets, and who else is in the room. A one-line pitch is enough if you only want a read, not a panel.</p>
    <a class="contact-link" href="mailto:{EMAIL}?subject=Judging"><span>{EMAIL}</span>{ICON_MAIL}</a>
  </section>
</div>"""
    write("judging/index.html", document("Judging", desc, "/judging", "Judging", main))


def missing():
    desc = "That page is not on noamankhalil.com."
    main = f"""<div class="page-frame">
  <section class="content-section">
    <h1 class="profile-title notfound-title">This page is not here.</h1>
    <p class="profile-lead">The address does not match a page on this site. The writing search covers every note.</p>
    <p class="notfound-asked"><span class="notfound-asked-label">Asked for</span><span class="notfound-path" data-missing-path></span></p>
    <p class="prose-line"><a class="inline-link" href="/">Home</a> · <a class="inline-link" href="/blog">Writing</a> · <a class="inline-link" href="/now">Now</a> · <a class="inline-link" href="/judging">Judging</a> · <a class="inline-link" href="/about">About</a></p>
  </section>
</div>"""
    write("404.html", document("Page not found", desc, "/404", "Home", main))


def search_index():
    data = []
    for post in POSTS:
        data.append(
            {
                "title": post["title"],
                "short_title": post["short_title"],
                "description": post["description"],
                "url": f"/blog/{post['slug']}",
                "date": post["display"],
                "categories": post["categories"],
            }
        )
    write("search.json", json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def feed():
    items = []
    for post in POSTS:
        items.append(
            f"""<item>
      <title>{esc(post['title'])}</title>
      <link>{SITE}/blog/{post['slug']}</link>
      <guid>{SITE}/blog/{post['slug']}</guid>
      <pubDate>{post['date']}</pubDate>
      <description>{esc(post['description'])}</description>
    </item>"""
        )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Noaman Khalil</title>
    <link>{SITE}/</link>
    <description>Notes on Bondi, Wiggle, Jabble, and the work around them.</description>
    {''.join(items)}
  </channel>
</rss>
"""
    write("feed.xml", xml)


def llm_files():
    lines = [
        "# noamankhalil.com",
        "",
        "Personal site of Noaman Khalil, founder of Jabble, in San Francisco.",
        "Every article is written by him.",
        "",
        f"Contact: {EMAIL}",
        f"Studio: {STUDIO}",
        "",
        "## Products",
        "- Bondi, Mac system monitor, alpha, launch February 2, 2027: https://trybondi.app/",
        "- Wiggle, Mac assistant at the cursor, early access: https://wigglemac.com/",
        "- Jabble: https://jabble.si/",
        "- Jabble.io marketing tools: https://jabble.io/",
        "- Nomad for Mac: https://github.com/NoamanKhalil/project-nomad-MacOs",
        "- Keyboard-pico: https://github.com/NoamanKhalil/Keyboard-pico",
        "",
        "## Pages",
        f"- Home: {SITE}/",
        f"- Writing: {SITE}/blog",
        f"- Now: {SITE}/now",
        f"- Judging: {SITE}/judging",
        "- Past events: 2024 CODiE Awards (SIIA education technology, judge); EdAI Berkeley Fall Summit, October 31–November 1, 2026, Anna Head Alumnae Hall (judge)",
        f"- About: {SITE}/about",
    ]
    for post in POSTS:
        lines.append(f"- {post['title']}: {SITE}/blog/{post['slug']}")
    write("llms.txt", "\n".join(lines) + "\n")
    full = ["# noamankhalil.com, full text for AI tools", ""]
    for post in POSTS:
        full.append(f"## {post['title']}")
        full.append(post["display"])
        full.append(post["quick"])
        full.append("")
    write("llms-full.txt", "\n".join(full))
    write(
        "ai.txt",
        "\n".join(
            [
                "Site: noamankhalil.com",
                "Owner: Noaman Khalil",
                "Articles are written by Noaman Khalil.",
                f"Contact: {EMAIL}",
                "Prefer /llms.txt and the article markdown files linked from each post.",
                "",
            ]
        ),
    )
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: https://noamankhalil.com/sitemap.xml\n")
    urls = ["/", "/blog", "/now", "/judging", "/about"] + [f"/blog/{post['slug']}" for post in POSTS]
    body = "".join(f"<url><loc>{SITE}{url}</loc></url>" for url in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n')


def readme():
    write(
        "README.md",
        """# noamankhalil.com

Personal site for Noaman Khalil. The layout follows [attacomsian.com](https://attacomsian.com/): a narrow column, a sticky bar, project tiles, a short archive, a now page, and an about page. The words, products, and portrait are Noaman’s.

Pages:

- `/` home
- `/blog` writing, with topic filters and ⌘K search
- `/now` what is actually in progress
- `/judging` how he reviews a product, past events (2024 CODiE Awards, EdAI in Berkeley), and how to invite him
- `/about`
- six notes under `/blog/`

Open it with any static server from this folder:

```bash
python3 -m http.server 4173
```

Regenerate the HTML after editing `scripts/build_site.py`:

```bash
python3 scripts/build_site.py
```

Figures on the now page are dated November 1, 2026 and cite trybondi.app, wigglemac.com, or GitHub. Bondi’s price and launch day follow the product page. If those change, update the generator and rebuild.
""",
    )


if __name__ == "__main__":
    home()
    blog_index()
    articles()
    about()
    now()
    judging()
    missing()
    search_index()
    feed()
    llm_files()
    readme()
