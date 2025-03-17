<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible";
  import { Button } from "$lib/components/ui/button";
  import * as Dialog from "$lib/components/ui/dialog";
  import { StickyNote } from "@lucide/svelte";
  import { ScrollArea } from "$lib/components/ui/scroll-area";

  let { children, referenceMessage, for: messageId } = $props();

  let open = $state(getQueryParameter() === messageId);

  $effect(() => {
    if (open) {
      setQueryParameter(messageId);
    } else {
      deleteQueryParameter();
    }
  });

  function setQueryParameter(messageId: string) {
    if (typeof window === "undefined") return;
    const url = new URL(window.location.href);
    url.searchParams.set("annotation", messageId);
    url.hash = "";
    window.history.pushState({}, "", url);
  }
  function deleteQueryParameter() {
    if (typeof window === "undefined") return;
    const url = new URL(window.location.href);
    url.searchParams.delete("annotation");
    window.history.pushState({}, "", url);
  }
  function getQueryParameter() {
    if (typeof window === "undefined") return;
    const url = new URL(window.location.href);
    return url.searchParams.get("annotation");
  }
</script>

<Dialog.Root bind:open>
  <Dialog.Trigger>
    <Button
      variant="ghost"
      class="gap-2 flex mx-auto"
      on:click={() => (open = !open)}
    >
      <StickyNote /> Annotation
    </Button></Dialog.Trigger
  >
  <Dialog.Content class="max-w-[600px]">
    <Dialog.Header class="max-h-[calc(100vh-10rem)]">
      <!-- <Dialog.Title>Are you sure absolutely sure?</Dialog.Title> -->
      {@render referenceMessage()}
      <!-- <ScrollArea> -->
      <ScrollArea class="pr-2">
        <Dialog.Description>
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
