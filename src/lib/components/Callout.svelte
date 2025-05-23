<script>
  import { TriangleAlert, OctagonAlert, Info } from "@lucide/svelte";
  const { color, children, icon = "info" } = $props();

  const _colorsForTailwind = {
    yellow:
      "text-yellow-400 bg-yellow-600/25 border-yellow-600/50 text-yellow-100/90",
    blue: "text-blue-400 bg-blue-600/25 border-blue-600/50 text-blue-100/90",
    sky: "text-sky-400 bg-sky-600/25 border-sky-600/50 text-sky-100/90",
    cyan: "text-cyan-400 bg-cyan-600/25 border-cyan-600/50 text-cyan-100/90",
    red: "text-red-400 bg-red-600/25 border-red-600/50 text-red-100/90",
  };

  const Icon = { warning: TriangleAlert, stop: OctagonAlert, info: Info }[icon];
</script>

<div
  class="bg-{color}-600/25 border-{color}-600/50 text-{color}-100/90 border-1 p-4 font-medium
 rounded-xl text-sm flex items-start gap-2"
>
  <Icon size="20" class="text-{color}-400  shrink-0" />
  <div>
    {@render children()}
  </div>
</div>
