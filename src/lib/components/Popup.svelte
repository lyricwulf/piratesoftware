<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog";
  import Button from "$lib/components/ui/button/button.svelte";
  import { ScrollArea } from "$lib/components/ui/scroll-area";
  import { SquareArrowOutUpRight } from "@lucide/svelte";

  const { preview, children } = $props();

  let open = $state(false);
</script>

<div class="popup-container w-fit">
  <Button
    variant="ghost"
    class="popup-small text-sm rounded-lg cursor-pointer font-bold flex
  items-center gap-2 softborder whitespace-normal h-auto min-h-9 text-start"
    onclick={() => (open = !open)}
    onkeydown={() => (open = !open)}
  >
    <SquareArrowOutUpRight size={18} />
    {#if preview}
      <div class="caption grow shrink-0 basis-0">
        {#if typeof preview === "function"}
          {@render preview()}
        {:else}
          {@html preview}
        {/if}
      </div>
    {/if}
  </Button>
</div>

<Dialog.Root bind:open>
  <!-- <Dialog.Trigger> -->
  <!-- <Button
     variant="ghost"
     class="flex gap-2 mx-auto mb-8"
     on:click={() => (open = !open)}
   >
     <StickyNote /> Annotation
   </Button> -->
  <!-- </Dialog.Trigger> -->
  <Dialog.Content class="max-w-[600px]">
    <Dialog.Header class="max-h-[calc(100vh-10rem)]">
      {#if typeof preview === "function"}
        {@render preview()}
      {:else}
        {@html preview}
      {/if}
      <ScrollArea class="pr-2 mt-1.5">
        <Dialog.Description class="markdown">
          {@render children()}
        </Dialog.Description>
      </ScrollArea>
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>

<style>
  @keyframes pop-up {
    0% {
      transform: scale(0.9);
      opacity: 0;
    }
    100% {
      transform: scale(1);
      opacity: 1;
    }
  }
</style>
