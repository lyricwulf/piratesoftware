<script>
  let { key, media } = $props();
  const ext = { sticker: "webp", photo: "jpg" }[media];
</script>

<div class={media}>
  <img src="/media/{media}/{key}.{ext}" alt={media} />
</div>

<style>
  .sticker {
    max-width: 200px;
  }
</style>
