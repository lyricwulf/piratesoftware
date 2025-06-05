<script lang="ts">
  import NavNode from "./NavNode.svelte";
  import "../app.css";
  import { NAV_ITEMS } from "./md-metadata";
  import { ScrollArea } from "$lib/components/ui/scroll-area";
  import { searchRefs } from "./search";
  import { Button } from "$lib/components/ui/button";
  import { Search } from "@lucide/svelte";

  const { class: className = "" } = $props();

  let t = $state<ReturnType<typeof setTimeout> | null>(null);
</script>

<nav
  class="sticky-top {className} flex flex-col gap-2"
  onmouseleave={() => {
    t = setTimeout(() => {
      window.dispatchEvent(new CustomEvent("resetNav"));
    }, 300);
  }}
  onmouseenter={() => {
    if (t) clearTimeout(t);
  }}
>
  <Button
    variant="ghost"
    onclick={() => {
      searchRefs.openSearch();
    }}
    class="gap-2 text-muted-foreground hover:bg-muted focus:bg-muted
  active:bg-muted border border-gray-600 justify-start mr-3"
  >
    <Search size={16} />
    Search
  </Button>
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

  nav :global([data-current="false"]) {
    opacity: 0.6;
    font-weight: 400;
  }

  nav :global([data-current="true"]) {
    color: hsl(var(--text));
    font-weight: 600;
    background-color: hsl(var(--muted));
  }
</style>
