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
  import { MD_METADATA } from "./md-metadata";
  import { Badge } from "$lib/components/ui/badge";

  let { name = "", children = [], href = "" } = $props();

  let current = $derived(page.url.pathname === href);
  let open = $state(
    page.url.pathname === href ||
      children.some((child) => child.href === page.url.pathname)
  );

  const metadata = $derived(MD_METADATA.get(href));
</script>

{#if name}
  {#if children?.length}
    <Collapsible.Root bind:open>
      <div class="collapsible">
        <Button
          class="justify-start font-bold text-foreground gap-2 cursor-pointer"
          variant="ghost"
          on:click={() => (open = !open)}
        >
          {#if open}
            <FolderOpen size={18} />
          {:else}
            <Folder size={18} />
          {/if}
          {name}
          <!-- <ChevronDown class="chevron" /> -->
        </Button>
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
  }
  :global([data-state="open"]) > .collapsible {
    background: hsl(var(--popover));
    border-radius: 5px;
    border: 1px solid hsl(var(--border));
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
