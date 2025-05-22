<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible";
  import { Button } from "$lib/components/ui/button";

  const { preview = "Click to view.", children } = $props();

  let open = $state(false);
</script>

<Collapsible.Root bind:open class="bg-popover p-4">
  <Collapsible.Trigger class="flex flex-col gap-2">
    {preview}
    <Button variant="ghost" class="softborder"
      >{open ? "(Click to hide)" : "(Click to show)"}</Button
    >
  </Collapsible.Trigger>
  <Collapsible.Content>
    {@render children()}
  </Collapsible.Content>
</Collapsible.Root>
