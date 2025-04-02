<script lang="ts">
  import { MESSAGES_BY_ID } from "$lib/messages";
  import ChatBubble from "$lib/components/ChatBubble.svelte";

  let { n } = $props();
  let message = $derived(MESSAGES_BY_ID.get(Number(n)));
  if (!message) {
    throw new Error(`Message with ID ${n} not found`);
  }
</script>

<ChatBubble {...message} />
