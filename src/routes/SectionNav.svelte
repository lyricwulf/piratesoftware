<script lang="ts">
  import "../app.css";
  import { page } from "$app/state";
  import { mdMetadata } from "$lib/__derived/metadata.json";
  import Button from "$lib/components/ui/button/button.svelte";
  import { onMount } from "svelte";
  import { replaceState, afterNavigate } from "$app/navigation";
  import { ChevronRight } from "@lucide/svelte";

  const { class: className = "" } = $props();

  let clientPath = $derived(page.url.pathname);
  let pageMetadata = $derived(mdMetadata[clientPath]);

  let currentSection = $state(
    typeof window !== "undefined" && window.location.hash
  );

  function setSection(section: string) {
    if (currentSection === section) return;
    currentSection = section;
    const location = window.location.toString().split("#")[0];
    replaceState(location + section, { hash: section });
  }

  function resetScroll() {
    window.scroll(0, 0);
  }

  let destroyCb = $state(() => {});
  function attachListener() {
    destroyCb?.();
    const headings = [...document.querySelectorAll("a")].filter((a) => {
      return `#${a.parentElement?.id}` === a.hash;
    });
    const scroll_cb = (e: Event) => {
      for (const ha of headings) {
        const rect = ha.getBoundingClientRect();
        if (rect.top >= 100 && rect.top <= 200) {
          if (currentSection === ha.hash) return;
          setSection(ha.hash);
          return;
        }
      }
    };

    document.addEventListener("scroll", scroll_cb, { passive: true });
    destroyCb = () => {
      document.removeEventListener("scroll", scroll_cb);
    };
    return () => destroyCb();
  }

  onMount(() => {
    attachListener();
  });

  afterNavigate(() => {
    attachListener();
    setSection(page.url.hash);
  });
</script>

<div class="sidebar sticky-top m-2 section-nav {className}">
  <ol>
    {#each pageMetadata?.headings as { level, title, slug }}
      <li>
        <Button
          onclickcapture={resetScroll}
          href={`#${slug}`}
          class="justify-start gap-1"
          variant="ghost"
          data-current={currentSection === `#${slug}`}
          onclick={() => setSection(`#${slug}`)}
        >
          <ChevronRight size="18" />
          {title}
        </Button>
      </li>
    {/each}
  </ol>
</div>

<style>
  .section-nav :global([data-current]) {
    transition:
      color 0.2s ease-in-out,
      background-color 0.2s ease-in-out,
      transform 0.3s var(--ease-out-expo),
      opacity 0.3s var(--ease-out-expo);
  }

  .section-nav :global([data-current] svg) {
    transition: width 0.3s var(--ease-out-expo);
  }
  .section-nav :global([data-current="true"]) {
    color: var(--color-foreground);
    font-weight: 600;

    background-color: hsl(var(--muted));
  }

  .section-nav :global([data-current="false"]) {
    transform: scale(0.95);
    opacity: 0.6;
    font-weight: 400;
  }

  .section-nav :global([data-current="false"] svg) {
    opacity: 0;
    width: 0;
  }

  div.sidebar {
    padding: 0.5rem;
  }
  ol li {
    list-style-type: none;
  }

  li :global(> a) {
    width: 100%;
    align-items: left;
  }

  ol {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
</style>
