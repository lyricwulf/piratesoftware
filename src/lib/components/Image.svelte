<script lang="ts">
  import { page } from "$app/state";
  const { src: srcProp, caption } = $props();

  const pathname = page.url.pathname;
  const src = `${pathname}/${srcProp}`;
</script>

<div class="image-container">
  <label>
    <div class="image-small">
      <img {src} alt={caption} width="300" height="300" />
      {#if caption}
        <div class="caption">{@html caption}</div>
      {/if}
    </div>
    <input type="checkbox" />
    <div class="image-large">
      <img {src} alt={caption} class="large-image" />
    </div>
  </label>
</div>

<style>
  .image-container {
    max-width: 300px;
    margin-inline: auto;
  }
  .image-container input {
    display: none;
  }

  .image-small {
    position: relative;
    display: flex;
    flex-direction: column;

    border-radius: 8px;
    overflow: hidden;
  }

  .image-small:has(.caption) {
    margin-block: 1px; /* or the box shadow may cut off */
    box-shadow: 0 0 2px 0.4px white;
  }

  .image-small .caption {
    background: hsl(var(--accent));
    padding: 5px;
    text-align: center;

    font-size: 0.8rem;
    color: var(--color-tooltip);
    word-break: break-word;
  }

  .image-large {
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
  .image-large img {
    max-width: 100vw;
    max-height: 100vh;
    animation: pop-up 0.3s var(--ease-out-expo);
  }

  .image-container:has(input:checked) .image-large {
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
