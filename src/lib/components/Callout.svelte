<script>
  import { TriangleAlert, OctagonAlert } from "@lucide/svelte";
  const { color, children, icon } = $props();

  const Icon = { warning: TriangleAlert, stop: OctagonAlert }[icon];
</script>

<div
  class="bg-{color}-600/25 border-1 p-4 font-medium border-{color}-600/50 text-{color}-100/90
 rounded-xl text-sm flex items-start gap-2"
>
  <Icon size="20" class="text-{color}-400  shrink-0" />
  <div>
    {@render children()}
  </div>
</div>
