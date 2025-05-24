<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog";
  import Button from "$lib/components/ui/button/button.svelte";
  import { ScrollArea } from "$lib/components/ui/scroll-area";

  const { preview, children } = $props();

  let open = $state(false);
</script>

<div class="popup-container">
  <Button
    class="popup-small"
    variant="secondary"
    onclick={() => (open = !open)}
  >
    {#if preview}
      <div class="caption">{@html preview}</div>
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
      {@html preview}
      <ScrollArea class="pr-2 mt-1.5">
        <Dialog.Description class="markdown">
          {@render children()}
        </Dialog.Description>
      </ScrollArea>
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>

<style>
  .popup-container {
    max-width: 300px;
  }
  .popup-container input {
    display: none;
  }

  .popup-small {
    position: relative;
    display: flex;
    flex-direction: column;

    border-radius: 8px;
    overflow: hidden;
  }

  .popup-small:has(.caption) {
    margin-block: 1px; /* or the box shadow may cut off */
    box-shadow: 0 0 2px 0px white;
  }

  .popup-small .caption {
    background: hsl(var(--accent));
    padding: 5px;
    text-align: center;

    font-size: 0.8rem;
    color: var(--color-tooltip);
    word-break: break-word;
  }

  .popup-large {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.8);
    z-index: 10;
    justify-content: center;
    align-items: center;
  }
  .popup-large img {
    max-width: 100vw;
    max-height: 100vh;
    animation: pop-up 0.3s var(--ease-out-expo);
  }

  .popup-container:has(input:checked) .popup-large {
    display: grid;
  }

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
