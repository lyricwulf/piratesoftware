<script lang="ts">
  import "../app.css";
  import "../log-message.ts";
  import PageNav from "./PageNav.svelte";
  import SectionNav from "./SectionNav.svelte";
  import HideOnMobile from "./HideOnMobile.svelte";
  import { ListTree, TableOfContents, History } from "@lucide/svelte";
  import { page } from "$app/state";
  import { mdMetadata } from "$lib/__derived/metadata.json";
  import WipNotice from "./WipNotice.svelte";
  import { ModeWatcher } from "mode-watcher";
  import LightSwitch from "./LightSwitch.svelte";
  import Search from "./Search.svelte";

  let { children } = $props();

  let clientPath = $derived(page.url.pathname);
  let pageMetadata = $derived(mdMetadata[clientPath]);

  let hasSections = $derived(pageMetadata?.headings?.length > 0);
</script>

<Search />

<ModeWatcher />
<LightSwitch class="self-end" />
<div class="x-wrapper">
  <HideOnMobile position="left">
    {#snippet buttonContent()}
      <ListTree size={24} />
    {/snippet}
    <PageNav />
  </HideOnMobile>

  <div class="markdown">
    <span class="flex flex-col items-start">
      <h1>{pageMetadata?.title}</h1>
      <span
        class="flex items-center gap-2 text-sm text-muted-foreground border py-1 px-4 rounded-full"
      >
        Last edited: {new Date(
          pageMetadata?.lastModified * 1000
        ).toLocaleString("en-US", {
          timeZone: "America/Los_Angeles",
          month: "short",
          day: "numeric",
          year: "numeric",
          hour: "numeric",
          minute: "2-digit",
        })}
        <a
          href="https://github.com/lyricwulf/piratesoftware/commits/main/src/routes{clientPath}"
          target="_blank"
          rel="noopener noreferrer external"
        >
          <History size="16" />
        </a>
      </span>
    </span>
    {#if pageMetadata?.wip}
      <WipNotice />
    {/if}
    {@render children()}
  </div>

  {#if hasSections}
    <HideOnMobile position="right">
      {#snippet buttonContent()}
        <TableOfContents size={24} />
      {/snippet}
      <SectionNav />
    </HideOnMobile>
  {/if}
</div>

<svelte:head>
  <title>PirateSoftware Sucks - {pageMetadata?.title}</title>
  <meta name="description" content={pageMetadata?.description} />
</svelte:head>

<style>
  .x-wrapper {
    padding: var(--page-padding);

    display: grid;
    grid-template-columns:
      minmax(300px, 400px)
      minmax(min(50%, 800px), 800px)
      minmax(300px, 400px);
    flex-direction: row;
    align-items: start;
    justify-content: center;
  }

  .markdown {
    max-width: min(800px, 100vw);
    padding: 20px;

    display: flex;
    flex-direction: column;
    gap: 1rem;

    color: hsla(var(--foreground) / 80%);
    border-inline: 1px solid hsl(var(--border));
  }

  @media (max-width: 1200px) {
    .x-wrapper {
      grid-template-columns: 1fr;
      padding: 0px;
    }

    .markdown {
      justify-self: center;
      border-inline: none;
    }
  }
</style>
