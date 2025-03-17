<script lang="ts">
  import { ChevronDown } from "@lucide/svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import * as Collapsible from "$lib/components/ui/collapsible";
  import { page } from "$app/state";
  import NavNode from "./NavNode.svelte";

  let { name = "", children = [], href = "" } = $props();

  let current = $derived(page.url.pathname === href);
  let open = $state(
    page.url.pathname === href ||
      children.some((child) => child.href === page.url.pathname)
  );
</script>

{#if name}
  {#if children?.length}
    <Collapsible.Root bind:open>
      <div class="collapsible">
        <Button
          class="hover:bg-transparent hover:underline justify-start font-bold text-foreground "
          variant="ghost"
          on:click={() => (open = !open)}
        >
          {name}
          <ChevronDown class="chevron" />
        </Button>
        <Collapsible.Content>
          {#if open}
            <div class="collapsible-children">
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
      class="hover:bg-muted hover:underline justify-start text-foreground"
      variant="ghost"
      data-current={current}
      {href}
    >
      {name}
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
    border-block: 1px solid hsl(var(--border));
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
    margin-block: 0.25rem;
    padding-inline-start: 1rem;
  }

  :global([data-current="true"]) {
    background-color: hsl(var(--muted));
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
