<script>
  import { MESSAGES_BY_ID } from "$lib/messages";
  import Message from "$lib/components/Message.svelte";
  import Media from "$lib/components/Media.svelte";
  import ChatBubble from "$lib/components/ChatBubble.svelte";
  let { from = 0, to = 0 } = $props();
</script>

<div class="messages">
  {#each Array.from({ length: Number(to) - Number(from) + 1 }, (_, i) => Number(from) + i) as n}
    {@const message = MESSAGES_BY_ID.get(n)}
    {#if message}
      <ChatBubble {...message} />
    {/if}
  {/each}
</div>
