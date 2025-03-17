<script>
  export let element;
  export let condition;
</script>

{#if condition}
  <svelte:element this={element} {...$$restProps}> <slot /> </svelte:element>
{:else}
  <slot />
{/if}
