<script lang="ts">
  import "../app.css";
  import PageNav from "./PageNav.svelte";
  import SectionNav from "./SectionNav.svelte";
  import HideOnMobile from "./HideOnMobile.svelte";
  import { ListTree, TableOfContents } from "@lucide/svelte";
  import { page } from "$app/state";
  import { MD_METADATA } from "./md-metadata";
  import WipNotice from "./WipNotice.svelte";

  let { children } = $props();

  let clientPath = $derived(page.url.pathname);
  let pageMetadata = $derived(MD_METADATA.get(clientPath));
</script>

<div class="x-wrapper">
  <HideOnMobile position="left">
    {#snippet buttonContent()}
      <ListTree />
    {/snippet}
    <PageNav />
  </HideOnMobile>

  <div class="markdown">
    <h1>{pageMetadata?.title}</h1>
    {#if pageMetadata?.wip}
      <WipNotice />
    {/if}
    {@render children()}
  </div>

  <HideOnMobile position="right">
    {#snippet buttonContent()}
      <TableOfContents />
    {/snippet}
    <SectionNav />
  </HideOnMobile>
</div>

<svelte:head>
  <title>PirateSoftware Sucks - {pageMetadata?.title}</title>
  <meta name="description" content={pageMetadata?.description} />
</svelte:head>

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
