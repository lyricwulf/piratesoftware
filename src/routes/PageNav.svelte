<script lang="ts">
  import NavNode from "./NavNode.svelte";
  import "../app.css";
  import { NAV_ITEMS } from "./md-metadata";
  import { ScrollArea } from "$lib/components/ui/scroll-area";
</script>

<nav class="sticky-top">
  <ScrollArea class="h-[calc(100vh-6rem)]">
    <div class="flex flex-col gap-1">
      <NavNode {...NAV_ITEMS} />
    </div>
  </ScrollArea>
</nav>

<style>
  nav {
    padding: 0.5rem;
    border-radius: var(--radius);
    background: hsl(var(--popover));
  }
</style>
