<script lang="ts">
  import ANNOTATIONS from "$lib/annotations";
  import AnnotationBlock from "$lib/components/AnnotationBlock.svelte";
  import Media from "$lib/components/Media.svelte";
  import ChatBubble from "$lib/components/ChatBubble.svelte";
  import * as Collapsible from "$lib/components/ui/collapsible";
  import { Info } from "@lucide/svelte";

  let {
    from = "",
    text = "",
    dt = 0,
    id = null,
    withDate = false,
    media = null,
    key = null,
    file = null,
    dialog = true,
    children = null,
  } = $props();

  const inProps = { from, text, dt, id, withDate, media, key, file, dialog };

  let useRight = from === "Lyric";
  let background = useRight
    ? "linear-gradient(315deg, #0D47A1 25%, #1565C0 75%)"
    : "linear-gradient(45deg, #263238 25%, #37474F 75%)";

  const link = `messages${file === 1 ? "" : file}.html#message${id}`;

  const messageId = id;

  const messageAnnotation = ANNOTATIONS.get(messageId || "");
  const annotation = {
    component: messageAnnotation?.default,
    ...messageAnnotation?.metadata,
  };

  const hasAnnotation = Boolean(messageAnnotation && !annotation?.comment);
  const useAnnotated = Boolean(annotation?.message);

  let timeStr = $derived(
    (() => {
      if (!dt) return "";
      let date = new Date(dt * 1000);
      if (!withDate) {
        return date.toLocaleTimeString("en-US", {
          hour: "numeric",
          minute: "numeric",
          hour12: true,
        });
      }
      return date.toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });
    })()
  );

  let open = $state(annotation?.comment ? true : (null as boolean));
  let chatBubble = $state<HTMLDivElement>(null);

  const clickHandler = () => {
    open = !open;
    navigator.clipboard.writeText(`annotation-${id}`); // TEMP!~
  };

  $effect(() => {});
</script>

<div
  class="chat-bubble text-sm"
  class:useRight
  class:hasAnnotation
  class:dialog
  style="background: {background}"
  onclick={clickHandler}
  onkeypress={clickHandler}
  role="button"
  tabindex="-1"
  bind:this={chatBubble}
>
  <div>
    {#if useAnnotated}
      {@html annotation?.message}
    {:else if text}
      {text}
    {/if}
    {#if media}
      <Media {media} {key} />
    {/if}
    {#if children}
      {@render children()}
    {/if}
  </div>
  {#if timeStr}
    <div class="chat-time text-xs text-gray-400 text-right">
      <a href="/archive/telegram/{link}" rel="external" target="_blank">
        {timeStr}
      </a>
    </div>
  {/if}
  {#if annotation?.comment}
    <div
      class="annotation-comment w-full"
      style="--comment-color: var(--{annotation.color})"
    >
      <Collapsible.Root {open}>
        <div class="flex items-center gap-2 font-bold">
          <Info class="shrink-0 basis-[20px]" />
          Comment
        </div>
        <Collapsible.Content>
          <div
            class="mt-2 pt-1 border-t-1 border-solid border-muted-foreground"
          >
            {@html annotation.comment}
          </div>
        </Collapsible.Content>
      </Collapsible.Root>
    </div>
  {/if}
</div>

{#if hasAnnotation && dialog}
  <AnnotationBlock
    {messageId}
    {open}
    onOpenChange={(newOpen) => (open = newOpen)}
    children={annotation.component}
  >
    {#snippet referenceMessage()}
      <ChatBubble {...inProps} dialog={false} />
    {/snippet}
  </AnnotationBlock>
{/if}

<style>
  :root {
    --red: hsla(0, 100%, 20%, 0.4);
    --yellow: hsla(45, 100%, 15%, 0.4);
  }
  a {
    color: hsl(var(--text)) !important;
  }

  .chat-bubble {
    position: relative;
    background-color: hsl(var(--muted));
    border-radius: 1rem 1rem 1rem 0;
    padding: 0.5rem 1rem;
    margin: 4px;
    width: fit-content;
    max-width: 70%;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;

    color: hsl(var(--foreground));
  }

  .chat-time {
    text-wrap: none;
    padding-inline-start: 0.2rem;
    margin-left: auto;
    justify-self: flex-end;
  }

  .chat-bubble:global(:has(.sticker)) {
    padding: 0.3rem;
  }

  .chat-bubble:global(:has(.sticker)) a {
    background: #000a;
    padding: 0.2rem 0.4rem;
    position: absolute;
    bottom: 0.2rem;
    right: 0.2rem;
    border-radius: 5px;
  }

  .chat-bubble :global(mark) {
    transition: background-color 0.2s;
  }

  .chat-bubble.dialog:not(:hover) :global(mark) {
    --mark-opacity: 0.1;
    /* background-color: transparent; */
  }

  :global(.annotation-comment *) {
    --mark-opacity: 0.4 !important;
  }

  .annotation-comment {
    /* color: var(--comment-color); */
    color: hsl(var(--muted-foreground));
    background: var(--comment-color, hsla(var(--popover) / 35%));
    border: 1px solid hsla(var(--muted-foreground) / 10%);
    padding: 0.5rem 1rem;
    border-radius: 5px;
    margin-top: 0.25rem;

    transition: border-color 0.2s;
  }

  .chat-bubble:hover .annotation-comment {
    border-color: hsla(var(--muted-foreground) / 40%);
  }

  .useRight {
    background-color: hsl(var(--accent));
    border-radius: 1rem 1rem 0 1rem;

    align-self: flex-end;
    margin-left: auto;
  }

  .chat-bubble.hasAnnotation.dialog {
    transition: transform 0.2s;
  }
  .chat-bubble.hasAnnotation.dialog:hover {
    cursor: pointer;
    transform: scale(1.01);
  }

  @media (max-width: 1200px) {
    .chat-bubble {
      max-width: 80%;
    }
  }
</style>
