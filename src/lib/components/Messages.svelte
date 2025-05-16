<script>
  import { MESSAGES_BY_ID } from "$lib/messages";
  import Message from "$lib/components/Message.svelte";
  import Media from "$lib/components/Media.svelte";
  import ChatBubble from "$lib/components/ChatBubble.svelte";
  let { from = 0, to = 0 } = $props();

  const messages = [];
  for (let i = Number(from); i <= Number(to); i++) {
    const message = MESSAGES_BY_ID.get(i);
    if (message) {
      messages.push(message);
    }
  }

  // partition messages by date
  const partitionedMessages = messages.reduce((acc, message) => {
    const date = new Date(message.dt * 1000).toDateString();
    if (!acc[date]) {
      acc[date] = [];
    }
    acc[date].push(message);
    return acc;
  }, {});
</script>

<div class="messages">
  <!-- {#each Array.from({ length: Number(to) - Number(from) + 1 }, (_, i) => Number(from) + i) as n}
    {@const message = MESSAGES_BY_ID.get(n)}
    {#if message}
      <ChatBubble {...message} />
    {/if}
  {/each} -->
  {#each Object.entries(partitionedMessages) as [date, messages]}
    <div class="date-group">
      <div class="date">{date}</div>
      {#each messages as message}
        <ChatBubble {...message} />
      {/each}
    </div>
  {/each}
</div>

<style>
  .messages {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background: hsl(var(--popover));
    padding: 0.25rem;
    border-radius: 0.5rem;
  }

  .date-group {
    display: flex;
    flex-direction: column;
    /* gap: 2px; */
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
