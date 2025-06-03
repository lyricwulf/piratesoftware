<script lang="ts">
  import Button from "$lib/components/ui/button/button.svelte";
  import { onNavigate } from "$app/navigation";

  let { children, buttonContent = null, position = "left" } = $props();

  let input: HTMLInputElement;

  onNavigate(() => {
    if (input) input.checked = false;
  });
</script>

<label class={position}>
  <input type="checkbox" bind:this={input} />
  <div class="drawer-btn">{@render buttonContent?.()}</div>
  <div class="close-shade"></div>
</label>
<div class="hide-on-mobile sticky-top {position}">{@render children()}</div>

<style>
  label {
    position: fixed;
    top: var(--page-padding);

    z-index: 9;
  }
  label > input {
    display: none;
  }
  label.left {
    left: var(--page-padding);
  }
  label.right {
    right: var(--page-padding);
  }

  .drawer-btn {
    background: hsl(var(--muted));
    padding: 1rem 1rem;
    border-radius: 8px;
    cursor: pointer;

    box-shadow: 0 0 10px 0 black;
  }

  @media (min-width: 1200px) {
    label {
      display: none;
    }
  }

  @keyframes from-left {
    from {
      transform: translateX(-100%);
    }
    to {
      transform: translateX(0);
    }
  }

  @keyframes from-right {
    from {
      transform: translateX(100%);
    }
    to {
      transform: translateX(0);
    }
  }

  @media (max-width: 1200px) {
    .hide-on-mobile {
      position: fixed;
      top: var(--page-padding);
      width: 300px;

      z-index: 11;

      background: hsl(var(--background));
      border: 1px solid hsl(var(--muted));
      border-radius: var(--radius);

      transition:
        transform 0.3s var(--ease-out-expo),
        opacity 0.3s var(--ease-out-expo);
    }

    .hide-on-mobile.left {
      --direction: -1;
      left: var(--page-padding);
    }
    .hide-on-mobile.right {
      --direction: 1;
      right: var(--page-padding);
    }

    label:not(:has(input:checked)) + .hide-on-mobile {
      opacity: 0;
      pointer-events: none;
      transform: translateX(calc(var(--direction) * 24px));
    }

    .close-shade {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.5);

      z-index: 10;
      transition: opacity 0.3s var(--ease-out-expo);
    }

    label:not(:has(input:checked)) .close-shade {
      opacity: 0;
      pointer-events: none;
    }

    /* fixes a z-index issue where the left shade will always show under the
       right button */
    :global(body:has(input:checked)) label .drawer-btn {
      display: none;
    }
  }
</style>
