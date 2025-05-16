<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import * as Dialog from "$lib/components/ui/dialog";
  import { StickyNote } from "@lucide/svelte";
  import { ScrollArea } from "$lib/components/ui/scroll-area";
  import { pushState } from "$app/navigation";
  import { tick, onMount } from "svelte";

  let {
    children,
    referenceMessage,
    messageId,
    open: extOpen,
    onOpenChange,
  } = $props();

  // NOTE: avoid setting the initial open state to true.
  // When open state is initially true, the dialog will be open at the start
  // but closing that dialog will cause the main body to be unscrollable.
  let open = $state(null as boolean);

  // setting the state after mount to circumvent the above issue
  onMount(() => {
    open = getQueryParameter() === String(messageId);
  });

  $effect(() => {
    if (typeof extOpen === "boolean") {
      open = extOpen;
    }
  });

  // sync the query parameter with the dialog state
  $effect(() => {
    void open; // dependency
    if (typeof open !== "boolean") return;
    tick().then(() => {
      if (open) {
        setQueryParameter(messageId);
      } else {
        deleteQueryParameter();
      }
    });
  });

  function setQueryParameter(messageId: string) {
    if (typeof window === "undefined") return;
    const url = new URL(window.location.href);
    url.searchParams.set("annotation", messageId);
    url.hash = "";
    pushState(url, {});
  }
  function deleteQueryParameter() {
    if (typeof window === "undefined") return;
    const url = new URL(window.location.href);
    url.searchParams.delete("annotation");
    pushState(url, {});
  }
  function getQueryParameter() {
    if (typeof window === "undefined") return;
    const url = new URL(window.location.href);
    return url.searchParams.get("annotation");
  }
</script>

<Dialog.Root bind:open {onOpenChange}>
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
      <!-- <Dialog.Title>Are you sure absolutely sure?</Dialog.Title> -->
      {@render referenceMessage()}
      <!-- <ScrollArea> -->
      <ScrollArea class="pr-2 mt-1.5">
        <Dialog.Description class="markdown">
          {@render children()}
        </Dialog.Description>
      </ScrollArea>
      <!-- </ScrollArea> -->
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>

<style>
  .annotation-block {
    padding: 20px;
    max-width: 800px;
    justify-self: center;
    /* color: hsla(var(--foreground) / 80%); */

    background: hsl(var(--popover));
  }
</style>
