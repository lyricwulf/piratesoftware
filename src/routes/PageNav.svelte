<script lang="ts">
  import NavNode from "./NavNode.svelte";
  import "../app.css";
  import { NAV_ITEMS } from "./md-metadata";
  import { ScrollArea } from "$lib/components/ui/scroll-area";

  const { class: className = "" } = $props();
</script>

<nav class="sticky-top {className}">
  <ScrollArea class="h-[calc(100vh-6rem)] pr-3">
    <div class="flex flex-col gap-2">
      <NavNode {...NAV_ITEMS} />
    </div>
  </ScrollArea>
</nav>

<style>
  nav {
    padding: 0.5rem;
    border-radius: var(--radius);
  }
  nav :global([data-current="true"]) {
    color: hsl(var(--text));
    font-weight: 600;
    background-color: hsl(var(--muted));
  }
</style>
