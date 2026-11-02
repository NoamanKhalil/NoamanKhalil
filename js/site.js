(function () {
  var themeKey = "theme";

  function currentTheme() {
    var set = document.documentElement.getAttribute("data-theme");
    if (set === "light" || set === "dark") return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function setupTheme() {
    var button = document.querySelector(".theme-button");
    if (!button) return;
    function label() {
      button.setAttribute(
        "aria-label",
        currentTheme() === "dark" ? "Switch to light theme" : "Switch to dark theme"
      );
    }
    button.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try {
        localStorage.setItem(themeKey, next);
      } catch (e) {}
      button.classList.remove("theme-anim");
      void button.offsetWidth;
      button.classList.add("theme-anim");
      label();
    });
    var media = window.matchMedia("(prefers-color-scheme: dark)");
    var onChange = function () {
      var stored = null;
      try {
        stored = localStorage.getItem(themeKey);
      } catch (e) {}
      if (!stored) label();
    };
    if (media.addEventListener) media.addEventListener("change", onChange);
    else if (media.addListener) media.addListener(onChange);
    label();
  }

  function setupMenu() {
    var button = document.querySelector(".menu-button");
    var overlay = document.querySelector(".menu-overlay");
    if (!button || !overlay) return;
    var links = overlay.querySelectorAll("a");
    function setOpen(open) {
      button.classList.toggle("is-open", open);
      button.setAttribute("aria-expanded", String(open));
      button.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      overlay.hidden = !open;
      document.body.classList.toggle("menu-open", open);
    }
    button.addEventListener("click", function () {
      setOpen(overlay.hidden);
    });
    overlay.addEventListener("click", function (event) {
      if (event.target === overlay) setOpen(false);
    });
    links.forEach(function (link) {
      link.addEventListener("click", function () {
        setOpen(false);
      });
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !overlay.hidden) setOpen(false);
    });
  }

  function setupSearch() {
    var button = document.querySelector(".search-button");
    var dialog = document.querySelector(".search-dialog");
    if (!dialog) return;
    var input = dialog.querySelector(".search-input");
    var close = dialog.querySelector(".search-close");
    var status = dialog.querySelector("[data-search-status]");
    var results = dialog.querySelector("[data-search-results]");
    var index = null;
    var previous = null;
    var active = -1;

    function norm(value) {
      return String(value || "").toLowerCase().trim();
    }
    function setStatus(text) {
      if (status) status.textContent = text;
    }
    function clearResults() {
      if (results) results.textContent = "";
      active = -1;
    }
    function resultItem(article, i) {
      var item = document.createElement("li");
      item.className = "search-result-item";
      item.setAttribute("role", "option");
      item.setAttribute("aria-selected", "false");
      item.id = "search-result-" + i;
      var link = document.createElement("a");
      link.className = "search-result-link";
      link.href = article.url;
      var title = document.createElement("span");
      title.className = "search-result-title";
      title.textContent = article.short_title || article.title;
      var meta = document.createElement("span");
      meta.className = "search-result-meta";
      meta.textContent = article.date;
      link.appendChild(title);
      link.appendChild(meta);
      item.appendChild(link);
      return item;
    }
    function move(next) {
      var items = results.querySelectorAll(".search-result-item");
      if (!items.length) return;
      if (next < 0) next = items.length - 1;
      if (next >= items.length) next = 0;
      active = next;
      items.forEach(function (item, i) {
        var on = i === active;
        item.classList.toggle("is-active", on);
        item.setAttribute("aria-selected", String(on));
        if (on) {
          input.setAttribute("aria-activedescendant", item.id);
          if (item.scrollIntoView) item.scrollIntoView({ block: "nearest" });
        }
      });
    }
    function render(matches, query) {
      clearResults();
      if (!query) {
        setStatus("Start typing to search articles.");
        input.setAttribute("aria-expanded", "false");
        return;
      }
      if (!matches.length) {
        setStatus("No articles found.");
        input.setAttribute("aria-expanded", "false");
        return;
      }
      setStatus(matches.length === 1 ? "1 article found." : matches.length + " articles found.");
      input.setAttribute("aria-expanded", "true");
      matches.slice(0, 8).forEach(function (article, i) {
        results.appendChild(resultItem(article, i));
      });
      move(0);
    }
    function haystack(article) {
      return norm([article.title, article.short_title, article.description, (article.categories || []).join(" ")].join(" "));
    }
    function score(article, words, query) {
      var title = norm(article.title);
      var shortTitle = norm(article.short_title);
      var text = article.searchText;
      var points = 0;
      for (var i = 0; i < words.length; i += 1) {
        if (text.indexOf(words[i]) === -1) return 0;
      }
      if (shortTitle === query || title === query) points += 80;
      if (shortTitle.indexOf(query) === 0 || title.indexOf(query) === 0) points += 40;
      if (shortTitle.indexOf(query) > -1 || title.indexOf(query) > -1) points += 20;
      return points + words.length;
    }
    function search(query) {
      var q = norm(query);
      if (!q || !index) return [];
      var words = q.split(/\s+/).filter(Boolean);
      return index
        .map(function (article) {
          return { article: article, score: score(article, words, q) };
        })
        .filter(function (row) {
          return row.score > 0;
        })
        .sort(function (a, b) {
          return b.score - a.score;
        })
        .map(function (row) {
          return row.article;
        });
    }
    function load() {
      if (index) return Promise.resolve(index);
      setStatus("Loading articles...");
      return fetch("/search.json")
        .then(function (response) {
          if (!response.ok) throw new Error("Search index request failed.");
          return response.json();
        })
        .then(function (data) {
          index = data.map(function (article) {
            article.searchText = haystack(article);
            return article;
          });
          return index;
        })
        .catch(function () {
          setStatus("Search is unavailable right now.");
          return [];
        });
    }
    function run() {
      render(search(input.value), input.value);
    }
    function setOpen(open) {
      if (button) button.setAttribute("aria-expanded", String(open));
      dialog.hidden = !open;
      document.body.classList.toggle("search-open", open);
      if (open) {
        previous = document.activeElement;
        load().then(function () {
          run();
          input.focus();
        });
      } else {
        input.value = "";
        input.removeAttribute("aria-activedescendant");
        clearResults();
        setStatus("Start typing to search articles.");
        if (previous && previous.focus) previous.focus();
      }
    }
    if (button) {
      button.addEventListener("click", function () {
        setOpen(dialog.hidden);
      });
    }
    if (close) {
      close.addEventListener("click", function () {
        setOpen(false);
      });
    }
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) setOpen(false);
    });
    input.addEventListener("input", run);
    input.addEventListener("keydown", function (event) {
      if (event.key === "ArrowDown") {
        event.preventDefault();
        move(active + 1);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        move(active - 1);
      } else if (event.key === "Enter") {
        var link = results.querySelector(".search-result-item.is-active a");
        if (link) {
          event.preventDefault();
          window.location.href = link.getAttribute("href");
        }
      }
    });
    results.addEventListener("click", function (event) {
      if (event.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (event) {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        setOpen(dialog.hidden);
        return;
      }
      if (event.key === "Escape" && !dialog.hidden) setOpen(false);
    });
  }

  function setupReveal() {
    var nodes = document.querySelectorAll(".page-frame:not(.reading-page) > *");
    if (!nodes.length) return;
    if (!("IntersectionObserver" in window) || document.hidden) {
      nodes.forEach(function (node) {
        node.classList.add("is-visible");
      });
      return;
    }
    var observer = new IntersectionObserver(
      function (entries) {
        var step = 0;
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var node = entry.target;
          node.style.transitionDelay = Math.min(step * 80, 320) + "ms";
          step += 1;
          node.classList.add("is-visible");
          observer.unobserve(node);
          node.addEventListener(
            "transitionend",
            function () {
              node.style.transitionDelay = "";
            },
            { once: true }
          );
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0 }
    );
    nodes.forEach(function (node) {
      observer.observe(node);
    });
    setTimeout(function () {
      nodes.forEach(function (node) {
        node.classList.add("is-visible");
      });
      observer.disconnect();
    }, 3000);
  }

  function setupTopics() {
    var chips = document.querySelectorAll(".topic-chip");
    if (!chips.length) return;
    var empty = document.querySelector(".archive-empty");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var topic = chip.getAttribute("data-topic");
        chips.forEach(function (other) {
          var on = other === chip;
          other.classList.toggle("is-active", on);
          other.setAttribute("aria-pressed", String(on));
        });
        document.querySelectorAll(".archive-year-item").forEach(function (item) {
          var topics = (item.getAttribute("data-topics") || "").split(/\s+/);
          item.hidden = topic !== "all" && topics.indexOf(topic) === -1;
        });
        document.querySelectorAll(".archive-year-group").forEach(function (group) {
          var visible = Array.prototype.some.call(group.querySelectorAll(".archive-year-item"), function (item) {
            return !item.hidden;
          });
          group.hidden = !visible;
        });
        if (empty) {
          empty.hidden = document.querySelectorAll(".archive-year-item:not([hidden])").length > 0;
        }
      });
    });
  }

  function setupMissing() {
    var path = document.querySelector("[data-missing-path]");
    if (path) path.textContent = location.pathname;
  }

  document.addEventListener("DOMContentLoaded", function () {
    setupTheme();
    setupMenu();
    setupSearch();
    setupReveal();
    setupTopics();
    setupMissing();
  });
})();
