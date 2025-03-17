<script>
  let {
    from = "",
    children,
    time = "",
    link = "",
    withDate = false,
  } = $props();

  let useRight = from === "Lyric";
  let background = useRight
    ? "linear-gradient(315deg, #0D47A1 25%, #1565C0 75%)"
    : "linear-gradient(45deg, #263238 25%, #37474F 75%)";

  let timeStr = $derived(
    (() => {
      let date = new Date(time);
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
</script>

<div
  class="chat-bubble text-sm"
  class:right={useRight}
  style="background: {background}"
>
  <div>
    {@render children()}
  </div>
  <div class="chat-time text-xs text-gray-400 text-right">
    <a href="/archive/telegram/{link}" rel="external">{timeStr}</a>
  </div>
</div>

<style>
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

  .right {
    background-color: hsl(var(--accent));
    border-radius: 1rem 1rem 0 1rem;

    align-self: flex-end;
    margin-left: auto;
  }

  @media (max-width: 1200px) {
    .chat-bubble {
      max-width: 80%;
    }
  }
</style>
