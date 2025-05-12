<script lang="ts">
  import { page } from "$app/state";
  const { src: srcProp, caption } = $$props;

  const pathname = page.url.pathname;
  console.log("test", pathname, srcProp);
  const src = `/src/routes${pathname}/${srcProp}`;
</script>

<div class="image-container">
  <label>
    <div class="image-small">
      <img {src} />
      {#if caption}
        <div class="caption">{caption}</div>
      {/if}
    </div>
    <input type="checkbox" />
    <div class="image-large">
      <img {src} alt="large image" class="large-image" />
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
  }

  .image-small .caption {
    background-color: linear-gradient(
      to top,
      rgba(0, 0, 0, 0.8) 0%,
      rgba(0, 0, 0, 0.8) 100%
    );
    color: white;
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
  }

  .image-container:has(input:checked) .image-large {
    display: grid;
  }
</style>
