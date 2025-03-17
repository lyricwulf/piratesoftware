<script>
  let { key, children, type } = $props();
</script>

<div class={type}>
  <img src="/{type}/{key}.webp" alt={type} />
</div>

<style>
  .sticker {
    max-width: 200px;
  }
</style>
