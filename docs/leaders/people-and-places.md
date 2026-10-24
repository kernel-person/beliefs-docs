# Manage people, places, and holy days

Founders and clergy open `/faith settings` to organize their community. Founder-only actions are identified below.

## Welcome people and appoint clergy

Open **People** and search by name. Choose **Invite** for an eligible person, **Approve** or **Decline** for an application, or **Withdraw** for an invitation. Players appear after they have joined the server.

Founders can select a member and choose **Make clergy** or **Remove clergy**. **Transfer** makes that member the founder and leaves the previous founder as clergy; review the confirmation before proceeding.

Joining policy belongs to **Identity** → **Membership**. See [creating a faith](create-faith.md) for the available policies.

## Register a temple

1. Stand where the worship area should be centered.
2. Open **Temples**, enter a name and radius, and choose **Create temple here**.
3. Share the temple's name with members. Selecting its entry starts navigation guidance.

The default radius is 12 blocks; the default server maximum is 64. Registration marks a worship area around your position. Ceremonies require it only when their own temple setting is enabled.

## Set a holy place

1. Look at a lodestone within six blocks.
2. Open **Holy place**, name it, and select **Save holy place** while still looking at the same lodestone.
3. If you changed targets, choose **Use lodestone** to refresh the viewed target first.

The founder can turn **Bonus: on** after a destination exists. Members can hold an ordinary compass and choose **Bind compass**. The facing bonus is optional; ordinary prayer works without it. See [prayer](../players/prayer.md).

**Clear target** asks for confirmation, removes the destination, and turns off its facing bonus.

## Plan a holy day

Open **Holy days** → **New holy day**, or use `/faith calendar manage`. Set a title and date, then choose an activity and repetition. **All-day observance** covers the whole local date; its start and duration fields are ignored. A saved ceremony or voluntary fast uses the start time and duration you enter. Optionally enable follower chat announcements, then **Save**.

**Once**, **Weekly** and **Yearly** use the entered date. **Western Easter** calculates Easter each year; the two **Umm al-Qura** options calculate the corresponding Eid. For calculated repeats, the entered date is the earliest allowed date. Regional observances can differ, so use **Once** for a locally published date.

The calendar uses real-world time in the displayed server timezone—Europe/London by default. An observance starts no ceremony or fast and awards no rewards. Participants still choose to begin scheduled activities; normal requirements and cooldowns apply.

The server-owned examples have [configurable default calendars](../server/configuration.md#example-holy-days). Saving or removing one through the editor preserves that community decision across restarts.

??? note "Calendar drafts and removal"

    **Back** keeps the calendar draft for **Continue draft**. Editing an existing holy day also requires **Save**. **Remove** asks for confirmation and removes that occasion and its future repeats. If its linked ceremony has been removed, choose a replacement activity.
