<script lang="ts">
  import NavNode from "./NavNode.svelte";
  import "../app.css";
  import { NAV_ITEMS } from "./md-metadata";

  console.log(NAV_ITEMS);
</script>

<nav class="sticky-top">
  <NavNode {...NAV_ITEMS} />
</nav>

<style>
  nav {
    padding: 0.5rem;
    border-radius: var(--radius);
    display: flex;
    flex-direction: column;
    gap: 4px;
    background: hsl(var(--popover));
  }
</style>
