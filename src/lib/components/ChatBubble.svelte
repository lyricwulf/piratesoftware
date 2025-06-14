<script lang="ts">
  import ANNOTATIONS from "$lib/annotations";
  import AnnotationBlock from "$lib/components/AnnotationBlock.svelte";
  import Media from "$lib/components/Media.svelte";
  import ChatBubble from "$lib/components/ChatBubble.svelte";
  import * as Collapsible from "$lib/components/ui/collapsible";
  import {
    Info,
    FolderOpen,
    ChevronRight,
    SquareArrowOutUpRight,
  } from "@lucide/svelte";
  import Callout from "$lib/components/Callout.svelte";
  import { page } from "$app/state";

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
    showFrom = false,
    comment = null,
  } = $props();

  // disable annotations, maybe enable in specific places
  dialog = false;

  const inProps = { from, text, dt, id, withDate, media, key, file, dialog };

  let useRight = { Lyric: true, Partner: true }[from] || false;
  let background =
    {
      Lyric: "linear-gradient(315deg, #0D47A1 25%, #1565C0 75%)",
      Shaye: "linear-gradient(315deg, rgb(120 53 15) 25%, rgb(69 26 3) 75%)",
      Partner: "linear-gradient(315deg, rgb(6 78 59) 25%, rgb(2 44 34) 75%)",
    }[from] || "linear-gradient(45deg, #263238 25%, #37474F 75%)";
  let showName =
    showFrom ||
    {
      Shaye: true,
      Partner: true,
    }[from] ||
    false;

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
          timeZone: "America/Los_Angeles",
          hour: "numeric",
          minute: "numeric",
          hour12: true,
        });
      }
      return date.toLocaleDateString("en-US", {
        timeZone: "America/Los_Angeles",
        month: "short",
        day: "numeric",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });
    })()
  );

  let open = $state<boolean | null>(annotation?.comment ? true : null);

  const clickHandler = () => {
    open = !open;
    navigator.clipboard.writeText(`${id}`); // TEMP!~
  };

  $effect(() => {});
</script>

<div
  class="chat-bubble text-sm text-gray-200 font-normal"
  class:useRight
  class:hasAnnotation
  class:dialog
  data-from={from}
  style="background: {background}"
  onclick={clickHandler}
  onkeypress={clickHandler}
  role="button"
  tabindex="-1"
>
  {#if showName}
    <div class="text-xs text-gray-100/60 mr-1">{from}:</div>
  {/if}
  <div class="break-word">
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

  {#if dialog && (annotation?.comment || annotation?.component || comment)}
    {@const isComment = annotation?.comment || comment}
    {@const Icon = isComment ? Info : SquareArrowOutUpRight}
    <div
      class="annotation-comment w-full text-gray-200/80"
      style="--comment-color: var(--{annotation?.color})"
    >
      <!-- unbound open to keep permanently open -->
      {#if isComment}
        <div class="text-xs flex items-start gap-2">
          <Icon size={18} class="inline shrink-0" />
          <div>
            {@html annotation?.comment || comment}
          </div>
        </div>
      {:else}
        <div class="flex items-center gap-1 font-bold">
          <Icon class="shrink-0 basis-[18px]" />
          {annotation?.title || (isComment ? "Comment" : "Annotation")}
        </div>
      {/if}
    </div>
  {/if}
</div>

{#if hasAnnotation && dialog}
  <AnnotationBlock
    {messageId}
    {open}
    onOpenChange={(newOpen: boolean) => (open = newOpen)}
    children={annotation.component}
  >
    {#snippet referenceMessage()}
      <ChatBubble {...inProps} dialog={false} />
    {/snippet}
  </AnnotationBlock>
{/if}

<style>
  :root {
    --red: color-mix(in oklab, var(--color-red-800) 40%, transparent 0%);
    --yellow: color-mix(in oklab, var(--color-yellow-800) 40%, transparent 0%);
  }
  a {
    color: hsl(var(--text)) !important;
  }

  .chat-bubble {
    position: relative;
    border-radius: 1rem 1rem 1rem 0;
    padding: 0.5rem 1rem;
    width: fit-content;
    max-width: 70%;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
  }

  :global(.chat-bubble[data-from="Thor"] + .chat-bubble[data-from="Lyric"]),
  :global(.chat-bubble[data-from="Lyric"] + .chat-bubble[data-from="Thor"]) {
    margin-top: 0.5rem;
  }

  .chat-time {
    text-wrap: none;
    padding-inline-start: 0.2rem;
    margin-left: auto;
    justify-self: flex-end;
  }

  .chat-bubble:global(:has(.telegram-media)) {
    padding: 0.3rem;
  }

  .chat-bubble:global(:has(.telegram-media)) a {
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
    --mark-opacity: 0.2;
    /* background-color: transparent; */
  }

  :global(.annotation-comment *) {
    --mark-opacity: 0.4 !important;
  }

  .annotation-comment {
    background: var(
      --comment-color,
      color-mix(in oklab, var(--color-gray-800) 60%, transparent 0%)
    );
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
  }

  @media (max-width: 1200px) {
    .chat-bubble {
      max-width: 80%;
    }
  }
</style>
