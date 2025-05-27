<script>
  let { key, media } = $props();
  const ext = { sticker: "webp", photo: "jpg" }[media];
</script>

<div class="telegram-media {media}">
  <img src="/media/{media}/{key}.{ext}" alt={media} />
</div>

<style>
  .sticker {
    max-width: 200px;
  }

  .photo {
    max-width: 200px;
    border-radius: 10px;
    overflow: hidden;
  }
</style>
