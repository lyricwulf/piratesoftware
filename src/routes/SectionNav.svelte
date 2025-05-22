<script lang="ts">
  import "../app.css";
  import { page } from "$app/state";
  import { MD_METADATA } from "./md-metadata";
  import Button from "$lib/components/ui/button/button.svelte";
  import { onMount } from "svelte";
  import { replaceState, afterNavigate } from "$app/navigation";

  let clientPath = $derived(page.url.pathname);
  let pageMetadata = $derived(MD_METADATA.get(clientPath));

  let currentSection = $state(
    typeof window !== "undefined" && window.location.hash
  );

  function setSection(section: string) {
    if (currentSection === section) return;
    currentSection = section;
    const location = window.location.toString().split("#")[0];
    replaceState(location + section, { hash: section });
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

<div class="sidebar sticky-top">
  <ol>
    {#each pageMetadata?.headings as { level, title, slug }}
      <li>
        <Button
          href={`#${slug}`}
          class="justify-start"
          variant="ghost"
          data-current={currentSection === `#${slug}`}
        >
          {title}
        </Button>
      </li>
    {/each}
  </ol>
</div>

<style>
  div.sidebar {
    background: hsl(var(--popover));
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
