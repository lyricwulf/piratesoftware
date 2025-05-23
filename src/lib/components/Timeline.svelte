<script>
  import {
    Timeline,
    TimelineItem,
    TimelineSeparator,
    TimelineDot,
    TimelineConnector,
    TimelineContent,
    TimelineOppositeContent,
  } from "svelte-vertical-timeline";

  const { items } = $$props;
</script>

<Timeline style="display: grid; grid-template-columns: max-content 1rem 1fr;">
  {#each items as [time, title, description]}
    <!-- <TimelineItem> -->
    <TimelineOppositeContent style="margin: 8px 4px 0 0;">
      <p class="time">{time}</p>
    </TimelineOppositeContent>
    <TimelineSeparator style="align-items: center;">
      <TimelineDot
        style="background-color: hsl(var(--primary)); align-self: center; width: 2px; height: 2px;"
      />
      <TimelineConnector style="background-color: hsl(var(--muted));" />
    </TimelineSeparator>
    <TimelineContent style="padding-bottom: 2rem; margin: 6px 0 0 4px; ">
      <div class="font-bold">{title}</div>
      <p class="text-sm">{description}</p>
    </TimelineContent>
    <!-- </TimelineItem> -->
  {/each}
</Timeline>

<style>
  :global(ul.timeline li::before) {
    content: none !important;
  }

  .time {
    font-size: 0.8rem;
    color: hsl(var(--muted-foreground));
    font-weight: 400;
  }
</style>
