<script lang="ts">
  import "../app.css";
  import PageNav from "./PageNav.svelte";
  import SectionNav from "./SectionNav.svelte";
  import HideOnMobile from "./HideOnMobile.svelte";
  import { ListTree, TableOfContents } from "@lucide/svelte";

  let { children } = $props();
</script>

<div class="x-wrapper">
  <HideOnMobile position="left">
    {#snippet buttonContent()}
      <ListTree />
    {/snippet}
    <PageNav />
  </HideOnMobile>

  <div class="markdown">
    {@render children()}
  </div>
  <HideOnMobile position="right">
    {#snippet buttonContent()}
      <TableOfContents />
    {/snippet}
    <SectionNav />
  </HideOnMobile>
</div>

<style>
  .x-wrapper {
    display: grid;
    grid-template-columns:
      minmax(300px, 400px)
      minmax(min(50%, 800px), 800px)
      minmax(300px, 400px);
    flex-direction: row;
    align-items: start;
    justify-content: center;
    padding: var(--page-padding);
  }

  .markdown {
    padding: 20px;

    max-width: min(800px, 100vw);
    justify-self: center;

    color: hsla(var(--foreground) / 80%);

    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  @media (max-width: 1200px) {
    .x-wrapper {
      grid-template-columns: 1fr;
    }
  }
</style>
