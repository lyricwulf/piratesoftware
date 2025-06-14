<script lang="ts">
  import {
    ChevronDown,
    FolderOpen,
    FolderClosed,
    Folder,
  } from "@lucide/svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import * as Collapsible from "$lib/components/ui/collapsible";
  import { page } from "$app/state";
  import NavNode from "./NavNode.svelte";
  import { mdMetadata } from "$lib/__derived/metadata.json";
  import { Badge } from "$lib/components/ui/badge";
  import { untrack } from "svelte";

  let { name = "", children = [], href = "" } = $props();

  let current = $derived(page.url.pathname === href);

  const shouldOpen = () =>
    page.url.pathname === href ||
    children.some((child) => child.href === page.url.pathname);

  let open = $state(shouldOpen());
  $effect(() => {
    void page.url;
    untrack(() => {
      open ||= shouldOpen();
    });
  });

  const metadata = $derived(mdMetadata[href]);
</script>

<svelte:window
  on:resetNav={() => {
    open = shouldOpen();
  }}
/>

{#if name}
  {#if children?.length}
    <Collapsible.Root bind:open>
      <div class="collapsible rounded-md">
        <Collapsible.Trigger
          class="flex gap-2 items-center py-2 px-4 hover:bg-muted text-sm
        transition rounded-md"
        >
          {#if open}
            <FolderOpen size={18} />
          {:else}
            <Folder size={18} />
          {/if}
          {name}
          <!-- <ChevronDown class="chevron" /> -->
        </Collapsible.Trigger>
        <Collapsible.Content>
          {#if open}
            <div class="collapsible-children pr-2 pb-2">
              {#each children as child}
                <NavNode {...child} />
              {/each}
            </div>
          {/if}
        </Collapsible.Content>
      </div>
    </Collapsible.Root>
  {:else}
    <Button
      class="hover:bg-muted justify-start text-foreground"
      variant="ghost"
      data-current={current}
      {href}
    >
      {name}
      {#if metadata?.wip}
        <Badge
          class="ml-2 border-1 bg-yellow-600/25 text-yellow-300
        border-yellow-600/50 hover:bg-yellow-600/50"
          variant="secondary">WIP</Badge
        >
      {/if}
      {#if metadata?.important}
        <Badge
          class="ml-2 border-1 bg-green-600/25 text-green-300
        border-green-600/50 hover:bg-green-600/50"
          variant="secondary">!</Badge
        >
      {/if}
    </Button>
  {/if}
{:else}
  {#each children as child}
    <NavNode {...child} />
  {/each}
{/if}

<style>
  .collapsible {
    border-block: 1px solid transparent;

    /* border-radius: 0.5rem; */
    display: flex;
    flex-direction: column;
    align-items: stretch;

    transition: opacity 0.3s var(--ease-out-expo);
  }
  .collapsible-children {
    transition:
      opacity 0.3s var(--ease-out-expo),
      transform 0.3s var(--ease-out-expo);
  }
  :global([data-state="open"]) > .collapsible {
    background: hsl(var(--popover));
    border: 1px solid hsl(var(--border));
  }
  :global([data-state="closed"]) > .collapsible {
    opacity: 0.6;
  }
  :global([data-state="closed"]) > .collapsible .collapsible-children {
    opacity: 0;
    transform: translateX(-20px);
  }

  .collapsible :global(a),
  .collapsible :global(button) {
    width: 100%;
    text-align: left;
  }

  .collapsible .collapsible-children {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    padding-inline-start: 2rem;
  }

  :global(.chevron) {
    transition: transform 0.2s;
    width: 1rem;
    height: 1rem;
    margin-left: auto;
  }

  :global([data-state="closed"] .chevron) {
    transform: rotate(-90deg);
  }
</style>
