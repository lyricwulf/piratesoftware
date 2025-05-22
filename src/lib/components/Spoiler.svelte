<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible";
  import { Button } from "$lib/components/ui/button";

  const { preview = "Click to view.", children } = $props();

  let open = $state(false);
</script>

<Collapsible.Root bind:open>
  <Collapsible.Trigger class="flex items-center gap-2">
    <Button variant="ghost" class="softborder">{preview}</Button>
    <span class="text-sm">{open ? "(Click to hide)" : "(Click to show)"}</span>
  </Collapsible.Trigger>
  <Collapsible.Content>
    {@render children()}
  </Collapsible.Content>
</Collapsible.Root>
