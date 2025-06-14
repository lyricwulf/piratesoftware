<script lang="ts">
  import { MESSAGES_BY_ID } from "$lib/messages";
  import ChatBubble from "$lib/components/ChatBubble.svelte";
  import { Badge } from "$lib/components/ui/badge";
  import * as Tooltip from "$lib/components/ui/tooltip";
  import { cn } from "$lib/utils";

  let {
    from,
    to = from,
    filterFrom,
    omit,
    annotations = true,
    scrollable = true,
    ns: messageIds = Array.from({ length: to - from + 1 }).map(
      (_, i) => i + Number(from)
    ),
  } = $props();

  const messages = [];
  for (const i of messageIds) {
    const message = MESSAGES_BY_ID.get(i);
    if (!message) continue;
    if (filterFrom && message.from !== filterFrom) continue;
    if (omit && omit.includes(message.id)) continue;
    messages.push(message);
  }

  // partition messages by date
  const partitionedMessages = messages.reduce(
    (acc, message) => {
      const date = new Date(message.dt * 1000).toLocaleDateString("en-US", {
        timeZone: "America/Los_Angeles",
        month: "short",
        day: "numeric",
        year: "numeric",
        weekday: "short",
      });
      if (!acc[date]) {
        acc[date] = [];
      }
      acc[date].push(message);
      return acc;
    },
    {} as Record<string, typeof messages>
  );
</script>

<div
  class={cn(
    "messages softborder",
    scrollable && "max-h-[min(60vh,600px)] overflow-y-auto"
  )}
>
  {#each Object.entries(partitionedMessages) as [date, messages]}
    <div class="date-group flex flex-col gap-1 px-2">
      <div class="date">{date}</div>
      {#if omit || !from}
        <Tooltip.Root openDelay={100}>
          <Tooltip.Trigger>
            <Badge class="text-xs" variant="secondary">
              Some messages may be omitted from this excerpt.
            </Badge>
          </Tooltip.Trigger>
          <Tooltip.Content
            class="bg-popover text-popover-foreground softborder"
          >
            <p>Best efforts were made to maintain all necessary context.</p>
            <p>
              Please refer to the transcript or archive for the full
              conversation.
            </p>
          </Tooltip.Content>
        </Tooltip.Root>
      {/if}
      {#each messages as message}
        <ChatBubble {...message} dialog={annotations} />
      {/each}
    </div>
  {/each}
</div>

<style>
  .messages {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background: var(--color-gray-950);
    padding: 0.25rem;
    border-radius: 0.5rem;
  }

  .date {
    font-size: 0.875rem;
    color: hsl(var(--muted-foreground));
    margin-top: 0.5rem;
    align-self: center;
    background: #fff1;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-weight: 500;
  }
</style>
