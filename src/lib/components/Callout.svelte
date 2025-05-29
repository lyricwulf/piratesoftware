<script>
  import {
    TriangleAlert,
    OctagonAlert,
    Info,
    ChevronRight,
    MessageCircleWarning,
  } from "@lucide/svelte";
  const { color, children, icon } = $props();

  const _colorsForTailwind = {
    yellow:
      "text-yellow-400 bg-yellow-600/25 border-yellow-600/50 text-yellow-100/90",
    blue: "text-blue-400 bg-blue-600/25 border-blue-600/50 text-blue-100/90",
    sky: "text-sky-400 bg-sky-600/25 border-sky-600/50 text-sky-100/90",
    cyan: "text-cyan-400 bg-cyan-600/25 border-cyan-600/50 text-cyan-100/90",
    red: "text-red-400 bg-red-600/25 border-red-600/50 text-red-100/90",
  };

  const Icon =
    {
      warning: TriangleAlert,
      stop: OctagonAlert,
      info: Info,
      alert: MessageCircleWarning,
    }[icon] || ChevronRight;
</script>

<div
  class="border-1 p-4 font-medium rounded-xl text-sm flex items-start gap-2"
  data-color={color}
>
  <Icon size="20" class="icon shrink-0" />
  <div class="flex flex-col gap-1.5">
    {@render children()}
  </div>
</div>

<style>
  :global([data-color="yellow"]) {
    background-color: color-mix(
      in oklab,
      var(--color-yellow-600) 25%,
      transparent 0%
    );
    border-color: color-mix(
      in oklab,
      var(--color-yellow-600) 50%,
      transparent 0%
    );
    color: color-mix(
      in oklab,
      var(--color-yellow-500) 40%,
      hsl(var(--foreground)) 60%
    );
  }
  :global([data-color="yellow"] strong) {
    color: color-mix(
      in oklab,
      var(--color-yellow-500) 15%,
      hsl(var(--foreground)) 85%
    );
  }
  :global([data-color="yellow"] .icon) {
    color: color-mix(
      in oklab,
      var(--color-yellow-500) 80%,
      hsl(var(--foreground)) 20%
    );
  }

  :global([data-color="blue"]) {
    background-color: color-mix(
      in oklab,
      var(--color-blue-600) 25%,
      transparent 0%
    );
    border-color: color-mix(
      in oklab,
      var(--color-blue-600) 50%,
      transparent 0%
    );
    color: color-mix(
      in oklab,
      var(--color-blue-500) 40%,
      hsl(var(--foreground)) 60%
    );
  }
  :global([data-color="blue"] strong) {
    color: color-mix(
      in oklab,
      var(--color-blue-500) 15%,
      hsl(var(--foreground)) 85%
    );
  }
  :global([data-color="blue"] .icon) {
    color: color-mix(
      in oklab,
      var(--color-blue-500) 80%,
      hsl(var(--foreground)) 20%
    );
  }

  :global([data-color="sky"]) {
    background-color: color-mix(
      in oklab,
      var(--color-sky-600) 25%,
      transparent 0%
    );
    border-color: color-mix(in oklab, var(--color-sky-600) 50%, transparent 0%);
    color: color-mix(
      in oklab,
      var(--color-sky-500) 40%,
      hsl(var(--foreground)) 60%
    );
  }
  :global([data-color="sky"] strong) {
    color: color-mix(
      in oklab,
      var(--color-sky-500) 15%,
      hsl(var(--foreground)) 85%
    );
  }
  :global([data-color="sky"] .icon) {
    color: color-mix(
      in oklab,
      var(--color-sky-500) 80%,
      hsl(var(--foreground)) 20%
    );
  }

  :global([data-color="cyan"]) {
    background-color: color-mix(
      in oklab,
      var(--color-cyan-600) 25%,
      transparent 0%
    );
    border-color: color-mix(
      in oklab,
      var(--color-cyan-600) 50%,
      transparent 0%
    );
    color: color-mix(
      in oklab,
      var(--color-cyan-500) 40%,
      hsl(var(--foreground)) 60%
    );
  }
  :global([data-color="cyan"] strong) {
    color: color-mix(
      in oklab,
      var(--color-cyan-500) 15%,
      hsl(var(--foreground)) 85%
    );
  }
  :global([data-color="cyan"] .icon) {
    color: color-mix(
      in oklab,
      var(--color-cyan-500) 80%,
      hsl(var(--foreground)) 20%
    );
  }

  :global([data-color="red"]) {
    background-color: color-mix(
      in oklab,
      var(--color-red-600) 25%,
      transparent 0%
    );
    border-color: color-mix(in oklab, var(--color-red-600) 50%, transparent 0%);
    color: color-mix(
      in oklab,
      var(--color-red-500) 40%,
      hsl(var(--foreground)) 60%
    );
  }
  :global([data-color="red"] strong) {
    color: color-mix(
      in oklab,
      var(--color-red-500) 15%,
      hsl(var(--foreground)) 85%
    );
  }
  :global([data-color="red"] .icon) {
    color: color-mix(
      in oklab,
      var(--color-red-500) 80%,
      hsl(var(--foreground)) 20%
    );
  }
</style>
